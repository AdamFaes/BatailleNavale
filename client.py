import socket

UDP_IP = "10.160.108.16"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    MESSAGE=input("Message : ")
    sock.connect((UDP_IP, UDP_PORT))
    sock.send(MESSAGE.encode())
#data,addr = sock.recv(1024)
##print(data.decode())

    data, addr= sock.recvfrom(1024)
    print("Message : ", data.decode())
