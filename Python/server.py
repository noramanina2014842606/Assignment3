import socket

s = socket.socket()
Server = 'localhost'
Port = 567
s.bind((Server,Port))
s.listen(5)
socket.SO_LINGER

while True:
    c,address = s.accept()
    print " We Got Connetion from  ", address
    c.send ("Hello, You are Connected \n")
    c.close()
    
            

