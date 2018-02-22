from moduletp4 import triSelection
from moduletp4 import getDistance
from moduletp4 import getPoiClosest
from moduletp4 import getPoiInRange
from moduletp4 import sort 
from moduletp4 import triSelection
from moduletp4 import partition
from moduletp4 import quicksort
from moduletp4 import readDB
from moduletp4 import sort_par_categorie 
from moduletp4 import afficher_les_categiries
import sys
import os


#je change de repertoire courant la ou se trouve mon ficher de BD
os.chdir("C:/Users/bonj/Desktop/python/tp44")


print(" Bonjour ".center(80,"*") )


print(" Reponse du tp4 par BENALI ".center(80,"*") )

print("")

print(" Reponse a ".center(50,"*") )

print("")

print("je considere int = 4 oct")

print("")

print("      charactere = 2 oct")

print("")

print("(16+8+8)*1000000= 24 000 000")

print("")
print(" Reponse b  ".center(50,"*") )
print("")
print("la largeur est 10 000 m")
print("")
print(" Reponse c  ".center(50,"*") )
print("")

print("pour couvrir entierement le plan il faut 100 000 point d interet ")
###################################################################################################################
###################################################################################################################

print("")
print(" 2 A readDB  ".center(70,"*") )
print(" je charge la base de donne  ".center(70,"*") )
print("")




result=readDB("point_dinteret.txt")
listglob=result[0]   # la liste globale de tuples [categorie, x, y]
np = result[1]  #le nombre de case de la liste qui presente le nombre de ligne
####################################################################################
#listglob,np=readDB("point_dinteret.txt") #cest une solution aussi
#################################################################################### 
print("tapez le numero correspondant a l'option souhaité".center(70,"*") )
print("")
print("1- rechercher le point d'intérêt le plus proche")
print("")
print("2- afficher le nombre de points d'intérêt par catégorie dans la base de données")
print("")
print("3- afficher le nombre de points d'intérêt par catégorie dans un rayon de 25, 50, 100, 250, 500m")
print("")
print("4- rechercher les 30 points d'intérêt les plus proches, triés du plus proche au plus éloigné")
print("")
print("5- rechercher tous les points d'intérêt dans un rayon de 25, 50, 100, 250, 500m, triés du plus proche")
print("au plus éloigné")
print("")
print(" que souhaitez vous  ".center(70,"*") )
print("")
choix=int(input("saisir une option "))
print("vous avez saisie ",choix)


def menu(choix1):
  print("")
  if choix1 == 1:
    print("vous souhaitez chercher par categorie ou non")
    choix_ou_non=str(input("1- oui tapez oui si non appuyer sur entrer directement  "))
    if len(choix_ou_non)==0:
      Xa=int(input("entrer votre position x"))
      Ya=int(input("entrer votre position y"))
      point_pret=getPoiClosest(listglob,Xa,Ya)  
      print("le point le plus pret :\n", point_pret[0])
    else:# je passe par le choix de la categorie 
      categorie_choisi,tab_catego=afficher_les_categiries()
      print("vous avez choisi -->",tab_catego[categorie_choisi])
      Xa=int(input("entrer votre position x"))
      Ya=int(input("entrer votre position y"))
      point_pret=getPoiClosest(listglob,Xa,Ya)
      print("102",point_pret[2],len(point_pret))
      tab_catego_trie=[]
      i = 0
      while i< len(point_pret):
        if point_pret[i][0]==tab_catego[categorie_choisi]:
          print("107",point_pret[i])
          tab_catego_trie.append(point_pret[i])
          i += 1
      j = 0 # Notre indice pour la boucle while
      while j < len(tab_catego_trie):
        print(tab_catego_trie[i])
        j += 1




      
   
    
    
####################################################################################
  elif choix1 == 2:
    
    # oui=str(input("1- oui tapez oui si non tapez entrer "))
    # non=str(input("2- non tapez rien"))
    # print("je vous affiche [categorie, nombre]\n")
    # if oui == oui:
    #categorie_choisi==str(input(" tapez votre categorie")) 
    
    occurence1=sort_par_categorie (listglob)
    i = 0 # Notre indice pour la boucle while
    while i < len(occurence1):
      print(occurence1[i])
      i += 1


###################################################################################  
  elif choix1 == 3:
    rayon=int(input("saisir un rayon: \n"))
    Xa=int(input("entrer votre position x: \n"))
    Ya=int(input("entrer votre position y: \n"))
    list_par_rayon=getPoiInRange(listglob,Xa,Ya, rayon)

    petit_list=sort_par_categorie (list_par_rayon)
    print("")
    print(petit_list[1])
    i = 0 # Notre indice pour la boucle while
    while i < len(petit_list)-1:
      print(petit_list[i])
      i += 1
####################################################################################         
  elif choix1 == 4:
    Xa=int(input("entrer votre position x: \n"))
    Ya=int(input("entrer votre position y: \n"))
    trent_point_pret=getPoiClosest(listglob,Xa,Ya)
    
    i = 0 # Notre indice pour la boucle while
    while i < 30:
      print(trent_point_pret[i])
      i += 1
######################################################################################      
  elif choix1 == 5:
    rayon=int(input("saisir un rayon: \n"))
    Xa=int(input("entrer votre position x:\n "))
    Ya=int(input("entrer votre position y:\n "))
    print("")
    list_par_rayon=getPoiInRange(listglob,Xa,Ya, rayon)
    
    i = 0 # Notre indice pour la boucle while
    while i < len(list_par_rayon):
      print(list_par_rayon[i])
      i += 1
  else:
    print("je vous invite a relire le message de choix\n ")
    choix1=int(input("saisir une option a nouveau : "))
    menu(choix1) 


  return
menu(choix)    




    