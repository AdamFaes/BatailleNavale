import socket

UDP_IP = "10.160.108.16"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))



data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
print ("Connexion :", data.decode())

SENS=("Entrer le sens du bateau (Haut/Bas/Gauche/Droite) ")
sock.sendto(SENS.encode(),addr)
data, addr = sock.recvfrom(1024)
sensc = data.decode()

LIG=("Entrer la ligne ")
sock.sendto(LIG.encode(),addr)
data, addr = sock.recvfrom(1024)
ligc=int(data)

COL=("Entrer la colonne ")
sock.sendto(COL.encode(),addr)
data, addr = sock.recvfrom(1024)
colc=int(data)

print("Sens du bateau :",sensc)
print("Ligne du bateau :",ligc)
print("Colonne du bateau :",colc)

senss=input("Entrer le sens du bateau : ")
ligs=int(input("Entrer la ligne du bateau : "))
cols=int(input("Entrer la colonne du bateau : "))

print("Sens du bateau :",senss)
print("Ligne du bateau :",ligs)
print("Colonne du bateau :",cols)

grilleC=[[0 for i in range(10)]for j in range(10)]
         
grilleS=[[0 for i in range (10)]for j in range(10)]

if (sensc=="Droite"):
    grilleC[ligc][colc]="X"
    grilleC[ligc][colc+1]="X"
    grilleC[ligc][colc+2]="X"
    grilleC[ligc][colc+3]="X"
    
elif (sensc=="Gauche"):
    grilleC[ligc][colc]="X"
    grilleC[ligc][colc-1]="X"
    grilleC[ligc][colc-2]="X"
    grilleC[ligc][colc-3]="X"

elif (sensc=="Haut"):
    grilleC[ligc][colc]="X"
    grilleC[ligc-1][colc]="X"
    grilleC[ligc-2][colc]="X"
    grilleC[ligc-3][colc]="X"

else:
    grilleC[ligc][colc]="X"
    grilleC[ligc+1][colc]="X"
    grilleC[ligc+2][colc]="X"
    grilleC[ligc+3][colc]="X"

if (senss=="Droite"):
    grilleS[ligs][cols]="X"
    grilleS[ligs][cols+1]="X"
    grilleS[ligs][cols+2]="X"
    grilleS[ligs][cols+3]="X"
    
elif (senss=="Gauche"):
    grilleS[ligs][cols]="X"
    grilleS[ligs][cols-1]="X"
    grilleS[ligs][cols-2]="X"
    grilleS[ligs][cols-3]="X"

elif (senss=="Haut"):
    grilleS[ligs][cols]="X"
    grilleS[ligs-1][cols]="X"
    grilleS[ligs-2][cols]="X"
    grilleS[ligs-3][cols]="X"

else:
    grilleS[ligs][cols]="X"
    grilleS[ligs+1][cols]="X"
    grilleS[ligs+2][cols]="X"
    grilleS[ligs+3][cols]="X"
    
partie = 0

while partie = 0:
    
    TIRL=("Entrer la ligne ou tirer ")
    sock.sendto(TIRL.encode(),addr)
    data, addr = sock.recvfrom(1024)
    Lig=int(data)

    TIRC=("Entrer la colonne ou tirer ")
    sock.sendto(TIRC.encode(),addr)
    data, addr = sock.recvfrom(1024)
    Col=int(data)

    if (grilleS[Lig][Col]=="X"):
        TOUCHE=("BATEAU TOUCHE")
        sock.sendto(TOUCHE.encode(),addr)
        print("BATEAU TOUCHE")
        grilleS[Lig][Col]="*"
    else:
        TOUCHE=("RATE")
        sock.sendto(TOUCHE.encode(),addr)
        print("RATE")
        grilleS[Lig][Col]="*"

    tirl=input("Entrer la ligne ou tirer : ")
    tirc=input("Entrer la colonne ou tirer : ")

    if (grilleC[tirl][tirc]=="X"):
        TOUCHE=("BATEAU TOUCHE")
        sock.sendto(TOUCHE.encode(),addr)
        print("BATEAU TOUCHE")
        grilleC[tirl][tirc]="*"
    else:
        TOUCHE=("RATE")
        sock.sendto(TOUCHE.encode(),addr)
        print("RATE")
        grilleC[tirl][tirc]="*"

    
    

    
    
        
        
    

