#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
 
import serial

porta = "COM7"
ser = serial.Serial(porta, 115200)
ser.write('5')
#ser.write(b'5') #Prefixo b necessario se estiver utilizando Python 3.X
ser.read()
