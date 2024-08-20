# JBS Technical Challenge

## Challenge 1 

### System Diagram

<img src="./images/JBS-System-Diagram.png">

### Recommended Power Supply

**LED Boards Power**

(12 boards * 1 Amp) * 24 Volts = 288 Watts 

**Splitter Power**

24 Volts * 0.13 Amp = 3.12 Watts

**Total Power**

288 + 3.12 = 291.12 Watts 

291.12 Watts / 24 Volts = 12.13 Amps 

Recommended power supply for 12 boards with a single splitter = 24v (DC) 13 Amps (312 Watts)

## LED Control Script 
<a href="./scripts/LEDboard.py">Control Script</a>

Here python's built in socket module has been used to send UDP packets over a network. RGBW LED values are mapped to different ports based on the data structure of colour message. Attempts have been made to make this scalable by taking an object oriented and modular approach; ensuring that multiple splitters could be used and synchronised. 

## LED Test Script 
<a href="./scripts/test.py">Test Script</a>

Unittest module has been used to instantiate the LEDboard class and run two test methods.
One method simulates a single splitter using 4 channels with 3 boards chained in each channel.
As the final piece is expected to be 50m in length, it's likely more than one splitter will be required, so a second method simulates the use of three splitters with the same channel/board configuration as the first method.

The test script sets the debug attribute in the LEDboard class to True to print the packet values. It also sets the IP base to 125.0.0. to allow for further terminal debugging through use of a test server that listens for UDP packets and prints the received information - this proved to be very useful in debugging. For testing with splitters, do not change the IP base attribute. 

## Challenge 2

There are a number of technologies that could achieve this. I would first ask what the fidelity of the tracking information needs to be, and what the output from the artwork will be. 

If you just want to track when people are within a 5m distance of the piece, then using distance measuring technologies such as infrared and ultra sonic sensors could be a viable option. These would have to be placed at intervals along the 50m. Spacing between sensors would have to be tested as interference can occur, especially with ultrasonic sensors. This could be a relatively cost effective method of sensing. 

Another technology that could be applied is infrared motion sensors that detect body heat and motion could be used. Again, as this is a long piece, these would have to be placed at intervals. It's also worth noting the environment in which the piece is displayed. If there ambient temperatures are similar levels to human body temperatures it could be difficult to detect people.

If you wanted higher fidelity motion tracking that could track body position, and even recognise poses, then computer vision technology could be an option. Python libraries such as openCV allow tracking of objects, along with plugins such as MediaPipe in touchDesigner. Again, due to the length of the piece it is likely that cameras will need to be placed at intervals to cover the whole piece. There is an obvious concern with privacy when using this technology, so to avoid capturing identities, placing cameras above people facing the floor could be an option. Additionally, using infrared cameras could allow for tracking to work in low lighting conditions. This option is likely more expensive than the previous options, however this will give you more information that could be used to make the piece more interactive. 
