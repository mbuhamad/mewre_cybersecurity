########################
#Engr. Mashal Buhamad
########################
# Python3 script for UDP msg sender

import socket
UDP_IP = "127.0.0.1" # set the up address of the local machine
UDP_PORT = 965		 #965 is Kuwait country code !
while True:
	MESSAGE = input('Enter your msg here:')
	MESSAGE = MESSAGE.encode('utf-8') 
	print('UDP target IP:',UDP_IP)
	print('UDP target port:',UDP_PORT)
	print('message sent:',MESSAGE.decode()) 
	sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
