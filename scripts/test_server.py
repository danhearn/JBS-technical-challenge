import socket

def udp_server(host='127.0.0.1', port=16661):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_sock:
        server_sock.bind((host, port))
        print(f"Listening on {host}:{port}")
        while True:
            data, addr = server_sock.recvfrom(4096)
            print(f"Received data from {addr}: {data}")

if __name__ == '__main__':
    udp_server()
