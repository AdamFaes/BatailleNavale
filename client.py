import socket

UDP_IP = "10.160.108.16"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


MESSAGE=("Connecté !")
sock.connect((UDP_IP, UDP_PORT))
sock.send(MESSAGE.encode())
#data,addr = sock.recv(1024)
##print(data.decode())

data, addr= sock.recvfrom(1024)
print("Message Serveur : ", data.decode())

sens=input()
sock.send(sens.encode())

data, addr= sock.recvfrom(1024)
print("Message Serveur : ", data.decode())

lig=input()
sock.send(lig.encode())

data, addr= sock.recvfrom(1024)
print("Message Serveur : ", data.decode())

col=input()
sock.send(col.encode())

data, addr= sock.recvfrom(1024)
