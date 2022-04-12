import socket
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 966        # The port used by the server
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    msg=input('What do you want to say to server:')
    msg=msg.encode()
    s.sendall(msg)
    data = s.recv(1024)
    print('recived:',data.decode())
