#!/usr/bin/env python
from serial import serial
from time import sleep
from sh import hostname
s = serial.serial()
s.baudrate = 9600
s.timeout = 0
s.port = "/div/ttyAMA0"

try:
	s.open()
except serial.serialexception, e:
	sys.stder.write("port could not be opened %r: %s\n" % (s.port,e))
	sys.exit(1)

s.write("$$$ALL,OFF\r")
time.sleep(0.5)
#coverting string 
while True:
	s.write("")
	time.sleep(0.5)
	s.write("")
	time.sleep(0.5)