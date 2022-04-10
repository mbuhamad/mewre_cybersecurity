########################
#Engr. Mashal Buhamad
########################
# Python3 script for TCP server.
import socket               # Import socket module
s = socket.socket()         # Create a socket object
host = '127.0.0.1' # Get local machine name
print (host)
port = 2345              # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from', addr)
   data = c.recv(1024)
   print (data)
   c.send(b'Thank you for connecting')
   c.close()                # Close the connection