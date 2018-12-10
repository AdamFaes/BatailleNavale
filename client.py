import socket

UDP_IP = "10.160.108.16"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

MESSAGE=("Connecté !")
sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))
data,addr = sock.recvfrom(1024)
print("",data.decode()) 
