#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
##print(s.recv(1024))

while True:
    data = s.recv(1024)
    if data == 'q' or data=='Q':
        s.close()
        break;
    else:
        print("RECIEVED:" , data)
        data = raw_input( "SEND( TYPE q or Q to Quit):")
        if data == 'Q' and data == 'q':
            s.send(data)
            s.close()
            break
        else:
            s.send(data)
