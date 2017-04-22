import socket
from threading import *

#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
host = socket.gethostname()                                   # Get local machine name
port = 12345                                                  # Reserve a port for your service.
s.bind((host, port))                                          # Bind to the port
   
class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while True:
            self.sock.send('Thank you for connecting')

s.listen(5)                                                   # Now wait for client connection.
print ('server started and listening')
while True:
    clientsocket, address = s.accept()                        # Establish connection with client.
    print 'Got connection from', address
    client(clientsocket, address)
    #client.close()                                            # Close the connection
