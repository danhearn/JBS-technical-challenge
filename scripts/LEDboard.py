import socket
from time import sleep

class LEDBoardControllerUDP:
    def __init__(self, splitter_ip_base='192.168.1.', splitter_ids=[128], udp_port=16661):
        """
        Initializes the LEDBoardControllerUDP with the given parameters.
        
        :param splitter_ip_base: Base IP address for the splitters.
        :param splitter_ids: List of IDs for the splitters.
        :param udp_port: UDP port for communication.
        """
        self.splitter_addresses = [(splitter_ip_base + str(splitter_id), udp_port) for splitter_id in splitter_ids]
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
    def send_packet(self, splitter_id, port_number, rgbw_data, num_of_ports=4, ports_in_pkt=1, start_frame=False):
        """
        Sends a packet to the specified splitter.
        
        :param splitter_id: ID of the splitter.
        :param port_number: Port number on the splitter (channel).
        :param rgbw_data: RGBW data to send.
        :param num_of_ports: Total number of ports to use on the splitter.
        :param ports_in_pkt: Number of ports covered by this packet.
        :param start_frame: Whether this packet starts a new frame.
        """
        format_byte = 0x00  # initial break DMX style
        flags = 0x80 if start_frame else 0x00 # start frame flag if start_frame is True else 0
        port_byte = port_number 
        nbytes = len(rgbw_data) # Number of bytes in the data
        # print(f"Data length for port {port_number}: {nbytes} bytes") #Debugging
        nports = num_of_ports # Number of ports in use on the splitter
        portsinpkt = ports_in_pkt # Number of ports covered by this packet
        
        packet = [
            0x02,  # Packet start byte
            format_byte,
            flags,
            port_byte,
            nbytes & 0xFF,  # Lower byte of nbytes
            (nbytes >> 8) & 0xFF,  # Upper byte of nbytes
            nports,
            portsinpkt
        ]
        packet.extend(rgbw_data)
        # print(f"Sending packet {packet} to splitter {splitter_id}, port {port_number}") Debugging
        splitter_address = self.splitter_addresses[splitter_id - 1]
        try:
            self.sock.sendto(bytearray(packet), splitter_address)
        except socket.error as e:
            print(f"Failed to send packet to splitter {splitter_id}: {e}")
    
    def broadcast_sync(self):
        """
        Sends a sync packet to all splitters on the network to for simultaneous data transmission.
        """
        sync_packet = [0x04]
        for splitter_address in self.splitter_addresses:
            try:
                self.sock.sendto(bytearray(sync_packet), splitter_address)
            except socket.error as e:
                print(f"Failed to send sync packet: {e}")
    
    def close(self):
        """ 
        Closes the socket connection.
        """
        self.sock.close()
    
    def map_colors_to_ports(self, splitter_id, port_colors):
        """
        Maps colors to ports on the specified splitter.

        :param splitter_id: The ID of the splitter to map the colors to.
        :param port_colors: A list of lists where each list contains colors for a specific port.
        """
        for port_number, colors in enumerate(port_colors, start=1):  # Port numbers start at 1
            rgbw_data = []
            for color in colors:
                if isinstance(color, list) and len(color) == 4:
                    rgbw_data.extend(color * 108)  # Extend data for all LEDs on the board (4 colors * 108 LEDs = 432 bytes)
                else:
                    raise ValueError(f"Invalid color format for port {port_number}: {color}")
            data_length = len(rgbw_data)
            # print(f"Data length for port {port_number}: {data_length} bytes") #Debugging
            self.send_packet(splitter_id, port_number, rgbw_data, start_frame=True)
        self.broadcast_sync()

    
    def color_cycle_test(self, splitter_ids, port_colors, delay=1.0):
        """
        Performs a color cycle test on the specified splitters.

        :param splitter_ids: List of splitter IDs.
        :param port_colors: A list of lists of colors for each port on each splitter.
        :param delay: Delay between color changes.
        """
        for splitter_id in splitter_ids:
            for color_pattern in port_colors:
                self.map_colors_to_ports(splitter_id, color_pattern)
                sleep(delay)
