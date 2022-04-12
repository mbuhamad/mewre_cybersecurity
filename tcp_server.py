########################
#Engr. Mashal Buhamad
########################
# Python3 script for TCP server.
import socket               # Import socket module
s = socket.socket()         # Create a socket object
host = '127.0.0.1'          # Get local machine name
print (host)
port = 966                  # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.
Trig=0                
while True:
   if Trig==0:
      c, addr = s.accept()     # Establish connection with client.
      print ('Got connection from', addr)
      Trig=1
   else:
      data = c.recv(1024)
      print (data.decode())
      msg=input('What do you want to say to client:')
      msg=msg.encode()
      c.send(msg)
      if data.decode()=='bye bye':
         c.close()
         break