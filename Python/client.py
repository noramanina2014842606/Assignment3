import socket
s = socket.socket()
server = '192.168.254.1'

port = 567
s.connect((server,port))
print s.recv(1024)
s.close()
