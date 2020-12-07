#First attempt to connect to FM305 through python
#isn't it cute, it's like a 'hello world' for this project. Clumsy, but it did a thing. finally. 
#With this code I am able to successfully connect to the reader, pass the U command encoded in ASCII
#it's basic, I need to do the work to bring everything to the next level. 
#-------------MAYDAY----------: this was just a test, you passed.
#Top Concern: I can see a good path, with documentation, in many directions to get started. Currently 
#the read rate is about 1 second. I need to understand better whats happening behind the scenes so I can 
#better understand my path forward to dramaically improve the speed. Hence my first attempts at logging,
#as can be seen. 

import serial
import time
import logging

logging.basicConfig(filename='dev_log', level=logging.DEBUG)


#configure port
ser = serial.Serial(
	port ='COM24', 
	baudrate = 38400,
	timeout = 1,
	parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE,
	bytesize =  serial.EIGHTBITS
	)

while ser.isOpen():	
	ser.write("U\r\n".encode('ascii'))

	s = ser.read(100)
	print(s)

	if s == b'\nU3400300833B2DDD9014000000000C41E\r\n\nU\r\n':
		break
	else:
		logging.debug('test')
