
 
from random import *
StockPaire=["A","A","B","B","C","C","D","D","E","E","F","F","G","G","H","H","I","I","J","J","K","K","L","L","M","M","N","N","O","O","P","P","Q","Q","R","R","S","S","T","T","U","U","V","V","W","W","X","X","Y","Y","Z","Z"]
Paires=input("nb depaire")
NbCase=Paires*2
Ligne=int(NbCase**0.5//1)
if Paires%2==0:
  Colonne=NbCase//(Ligne)
else:
  Colonne=NbCase//(Ligne-1)
def grille():
  if Paires%2==0:
    Horizontal=(Ligne)*["?"]
    for i in range(len(Horizontal)):
      Horizontal[i] = Colonne*["?"]
    return Horizontal
  else:
    Horizontal=(Ligne-1)*["?"]
    for i in range(len(Horizontal)):
      Horizontal[i] =Colonne*["?"]
    return Horizontal
 
def affich_grille():
  Horizontal=grille()
  for i in Horizontal:
    for j in i:
      print j++ " ",
    print ""
 
def remplir_grille():
  Possib=[]
  Possib=StockPaire[0:2*Paires]
  shuffle(Possib)
 
  return Possib
def formepaire():
  Possib=[]
  Possib=StockPaire[0:2*Paires]
  shuffle(Possib)
  if Paires%2==0:
    Horizontal=(Possib[0:Ligne])
    for i in range(len(Horizontal)):
      Horizontal[i] = Possib[0:Colonne]
    return Horizontal
  else:
    Horizontal=(Ligne-1)*["?"]
    for i in range(len(Horizontal)):
      Horizontal[i] =Colonne*["?"]
    return Horizontal
 
def affich_Paires():
  Horizontal=remplir_grille()
  for i in Horizontal:
    for j in i:
      print j+" ",
    print ""
