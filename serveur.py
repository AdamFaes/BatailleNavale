import socket

UDP_IP = "10.160.108.16"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))



data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
print ("Connexion :", data.decode())

SENS=("Entrer le sens du bateau (Haut/Bas/Gauche/Droite) ")
sock.sendto(SENS.encode(),addr)
sensc, addr = sock.recvfrom(1024)

LIG=("Entrer la ligne ")
sock.sendto(LIG.encode(),addr)
ligc, addr = sock.recvfrom(1024)

COL=("Entrer la colonne ")
sock.sendto(COL.encode(),addr)
colc, addr = sock.recvfrom(1024)

print("Sens du bateau :",sensc.decode())
print("Ligne du bateau :",ligc.decode())
print("Colonne du bateau :",colc.decode())

senss=input("Entrer le sens du bateau : ")
ligs=input("Entrer la ligne du bateau : ")
cols=input("Entrer la colonne du bateau : ")

print("Sens du bateau :",senss)
print("Ligne du bateau :",ligs)
print("Colonne du bateau :",cols)




