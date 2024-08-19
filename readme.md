# JBS Technical Challenge

## Challenge 1 

### System Diagram

<img src="./images/">

### Recommended Power Supply

**LED Boards Power**

(12 boards * 1 Amp) * 24 Volts = 288 Watts 

**Splitter Power**

24 Volts * 0.13 Amp = 3.12 Watts

**Total Power**

288 + 3.12 = 291.12 Watts 

291.12 Watts / 24 Volts = 12.13 Amps 

Recommended power supply for 12 boards with splitter = 24v (DC) 13 Amps (312 Watts)

## LED Control Script 
<a href="./scripts/LEDboard.py">Control Script</a>

Here I have used python's built in socket module to send UDP packets over a network. RGBW LED values are mapped to different ports based on the data structure of colour message. Attempts have been made to make this scalable by taking an object oriented and modular approach; ensuring that multiple splitters could be used and synchronised. 

## LED Test Script 

Unittest module has been used to instantiate the LEDboard class and run a test method. It passes a set of colour values to be sent over the network.

To test and debug scripts a test server was also created to allow visualisation of data being sent - this proved to be very useful in debugging.


## Challenge 2

