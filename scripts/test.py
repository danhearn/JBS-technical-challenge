import unittest
from LEDboard import LEDBoardControllerUDP 

class TestLEDBoardControllerUDP(unittest.TestCase):
    def setUp(self):
        # Initialise the controller with mock splitter IDs for the test_server.py script
        self.single_controller = LEDBoardControllerUDP(splitter_ids=[1], splitter_ip_base='127.0.0.', debug=True)
        self.multiple_controllers = LEDBoardControllerUDP(splitter_ids=[1, 2, 3], splitter_ip_base='127.0.0.', debug=True)
        self.port_colors = [
            [
                [255, 0, 0, 0],  # Port 1: Red for Node 1
                [0, 255, 0, 0],  # Port 1: Green for Node 2
                [0, 0, 255, 0],  # Port 1: Blue for Node 3
            ],
            [
                [255, 255, 0, 0],  # Port 2: Yellow for Node 4
                [0, 255, 255, 0],  # Port 2: Cyan for Node 5
                [255, 0, 255, 0],  # Port 2: Magenta for Node 6
            ],
            [
                [255, 255, 255, 0],  # Port 3: White for Node 7
                [128, 128, 128, 0],  # Port 3: Gray for Node 8
                [64, 64, 64, 0],     # Port 3: Dark Gray for Node 9
            ],
            [
                [255, 0, 0, 255],  # Port 4: Red with White for Node 10
                [0, 255, 0, 255],  # Port 4: Green with White for Node 11
                [0, 0, 255, 255],  # Port 4: Blue with White for Node 12
            ]
        ]

    def test_color_cycle_test(self):
        self.single_controller.color_cycle_test(splitter_ids=[1], port_colors=[self.port_colors], delay=1.0)
        
    def test_multiple_splitters(self):
        self.multiple_controllers.color_cycle_test(splitter_ids=[1, 2, 3], port_colors=[self.port_colors], delay=1.0)

    def tearDown(self):
        self.single_controller.close()
        self.multiple_controllers.close()

if __name__ == '__main__':
    unittest.main()