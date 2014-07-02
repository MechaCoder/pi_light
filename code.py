#!/usr/bin/env python
import serial
import time
#import sh
from sh import hostname
s = serial.serial()
s.baudrate = 9600
s.timeout = 0
s.port = "/div/ttyAMA0"

try:
	s.open()
except serial.serialexception, e:
	sys.stder.write("port could not be opened %r: %s\n" % (s.port,e))
#write the code to print