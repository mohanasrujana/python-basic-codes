import socket

host='localhost'
port=4000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host,port))
print("Server listening on port:",port)
s.listen(1)
# 1 indicates no. of connections

c,addr =  s.accept()
#c is client
print("Connection from:",str(addr))

c.send(b"Hello, how are you")
c.send("bye".encode())
c.close()