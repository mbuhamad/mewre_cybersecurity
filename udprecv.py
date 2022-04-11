########################
#Engr. Mashal Buhamad
########################
# Python3 script for UDP msg reciver

import socket 
UDP_IP = "127.0.0.1" #set the IP address of the machine
UDP_PORT = 965		 #965 is Kuwait country code !
mylist=(UDP_IP,UDP_PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(mylist) 
while True:
	data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
	print("received message:"+data.decode())