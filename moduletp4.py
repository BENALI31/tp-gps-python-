from math import sqrt,pow
from operator import itemgetter
from collections import Counter


# la fonction prend en entrée un fichier (dbFileName) de base de données 
# la fonction retourne la liste globale lg contenant les points d'intéret de la base et le nombre (np) de points trouvés 

def readDB(dbFileName):
    # on utilise le mot-clé with open pour ouvrir le fichier et fermer apres utilisation 
    with open(dbFileName) as f:
        pois = f.readlines()# elle stock les lignes dans une liste appeler pois 
    
    np = len(pois)  #le nombre de case de la liste qui presente le nombre de ligne 
    lg = [None]*np  

    for ind in range(np):
        poi = pois[ind]
        proprietes = poi.split("|")
        #affectation des fraquement de lignes au tuple de proprieté 
        categorie = str( proprietes[0] )
        x = int( proprietes[1] )
        y = int( proprietes[2] )

        lg[ind] =  [categorie, x, y]
      

    return lg,np # retourne

#######################################################################################################
# je cherche le point dinteret le plus proche

def getDistance(ma_posi_xx,ma_posi_yy,xlist,yliste):

    distance=((ma_posi_xx-xlist)**2)+((ma_posi_yy-yliste)**2)
   
    distance=sqrt(distance)
    
    return distance # retourne la distance entre les deux points



#####################################################################################################

# la fonction qui nous retourne le point le plus proche 

def getPoiClosest(tab,ma_posi_xx,ma_posi_yy):
    # je parcour mon tableau de tuples de point dinteret 
    for ind in range(len(tab)):
        #j'affecte chaque partie du tuple a un tableau tab 
        tab_tuple = tab[ind]

        categorie = tab_tuple[0]
        x = tab_tuple[1]
        y = tab_tuple[2] 
        
        distance=getDistance(ma_posi_xx,ma_posi_yy,x,y)
  # pour une meilleur lisibilité je fait un arondissement de 4 chiffres
        distance=round(distance,4)
  # j'affecte la distance a mon tableau de tuples et pour une bonne lisibilite je rajoute  "la distance est" dans le tuple 
        tab[ind] =  [categorie, x, y,"d'une distance de",distance]
        
    tab.sort(key=itemgetter(4))    
  
    return (tab) #je retourne le point le plus pret 

########################################################################################################################

def getPoiInRange(tab,ma_posi_xx,ma_posi_yy, threshold):

    tab1=[]
    indi_tab1= -1

    # je parcour mon tableau de tuples de point dinteret 
    for ind in range(len(tab)):
        #j'affecte chaque partie du tuple a un tableau tab 
        tab_tuple = tab[ind]

        categorie = tab_tuple[0]
        x = tab_tuple[1]
        y = tab_tuple[2] 
        
        distance=getDistance(ma_posi_xx,ma_posi_yy,x,y)
  # pour une meilleur lisibilité je fait un arondissement de 4 chiffres
        distance=round(distance,4)

        if distance<= threshold :
            indi_tab1= +1
      # j'affecte la distance a mon tableau de tuples et pour une bonne lisibilite je rajoute  "la distance est" dans le tuple 
            tab1.append([categorie, x, y,"d'une distance de",distance])
    # je trie mon nouveau tableau qui respect le rayon de distance  
    tab1.sort(key=itemgetter(4))

    return tab1
####################################################################################################################
## la fonction qui retourne les points d'intérêt par catégorie dans la base de données
def sort_par_categorie (tab):
    # je tri mon tableau par categorie
    tab.sort(key=itemgetter(0))
    occurence= 1
    tab_ocurence=[] # je cree une liste de tuple
    i = 0 # Notre indice pour la boucle while
    
    while i < len(tab)-1:

        if tab[i][0]==tab[i+1][0] : #je compare le courant avec le suivant 

            occurence+= 1
            i += 1 # On incrémente 
            if  i==len(tab)-1 :
                tab_ocurence.append([tab[i][0],occurence])
                occurence=1
                i += 1 # On incrémente
        else:
            tab_ocurence.append([tab[i][0],occurence])
            occurence=1
            i += 1 # On incrémente 

    return tab_ocurence

####################################################################################################################
def sort (tab,ma_posi_xx,ma_posi_yy):
    # je parcour mon tableau de tuples de point dinteret 
    for ind in range(len(tab)):
        #j'affecte chaque partie du tuple a un tableau tab 
        tab_tuple = tab[ind]

        categorie = tab_tuple[0]
        x = tab_tuple[1]
        y = tab_tuple[2] 
        
        distance=getDistance(ma_posi_xx,ma_posi_yy,x,y)
  # pour une meilleur lisibilité je fait un arondissement de 4 chiffres
        distance=round(distance,4)
  # j'affecte la distance a mon tableau de tuples et pour une bonne lisibilite je rajoute  "la distance est" dans le tuple 
        tab[ind] =  [categorie, x, y,"la distance est",distance]
        
    #gh=triSelection(tab)    
    gh=quicksort(tab, 0, len(tab)-1)
    return (gh) #je retourne tout les point les point le plus pret dans lordre croissant


    ######################################################################################################################
##
def triSelection(tableau):
    nb = len(tableau)
    for en_cours in range(0,nb):    
        plus_petit = en_cours
        for j in range(en_cours+1,nb) :
            if tableau[j][4] < tableau[plus_petit][4] :
                plus_petit = j
        if min is not en_cours :
            temp = tableau[en_cours]
            tableau[en_cours] = tableau[plus_petit]
            tableau[plus_petit] = temp
    return (tableau)


##################################################################################################################

#######################################################################################################




def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    right = end
    done = False
    while not done:
            while left <= right and myList[left][4] <= pivot[4]:
                left = left + 1
            while myList[right][4] >= pivot[4] and right >=left:
                right = right -1
            if right < left:
                done= True
            else:
                # swap places
                temp=myList[left]
                myList[left]=myList[right]
                myList[right]=temp
                # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp    
    return right    

def quicksort(myList, start, end):
    if start < end:
                # partition the list
                pivot = partition(myList, start, end)
                # sort both halves
                quicksort(myList, start, pivot-1)
                quicksort(myList, pivot+1, end)
    return myList
            

##################################################################################################################
######################## afficher les categiries 
def afficher_les_categiries():
    print("je vous affiche la liste de  point dinteret")
    print("je vous invite a cliquer sur le chiffre correspondant")
    les_categ=["Gaz_station","Mini_Market","Mall","Hospital","Hotel","Restaurant","Cinema","Parking","Bar"]
    i = 0 # Notre indice pour la boucle while
    while i < len(les_categ):
      print("-->",i,"-->",les_categ[i])
      i += 1
    print("")
    categorie_choisi=int(input("entrer votre choix et valider par entrer: \n"))
    return categorie_choisi,les_categ

##################################################################################################################
