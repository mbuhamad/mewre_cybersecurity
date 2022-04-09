import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 965
while True:
	MESSAGE = input("Enter your msg here:")
	MESSAGE = MESSAGE.encode('utf-8') 
	print("UDP target IP: %s" % UDP_IP)
	print("UDP target port: %s" % UDP_PORT)
	print("message: %s" % MESSAGE.decode()) 
	sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
