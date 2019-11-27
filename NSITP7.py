# -*- coding: utf-8 -*-

import codecs ## On importe codecs qui permet de lire un fichier en spécifiant l'encondage
import pprint ## On importe ppprint qui permet d'afficher des listes efficacement
import csv ## On importe csv qui permet de lire les fichiers .csv

def charger_table(nom): ## On définit la fonction charger_table qui prend en argument un string, nom et qui ouvre le fichier qui dispose de ce nom
    csvfile = codecs.open(nom, encoding='utf-8') ## On ouvre le fichier avec un encodage utf-8 grâce à codecs
    lecteurcsv = csv.reader(csvfile,delimiter=';') ## On lit le resultat de l'ouverture du fichier à l'aide de la mathode reader de csv

    tab=[] ## On déclare tab, la variable est un array et va contenir la 'table' comme définie dans l'énoncé (liste de tuples)
    for ligne in lecteurcsv: ## On lit chaque ligne du fichier csv ouvert
        tab.append(tuple(ligne)) ## On met les éléments de la ligne dans un tuple
    return tab ## On renvoie la liste de tuples, la 'table' comme définie dans l'énoncé

tablePays=charger_table("pays.csv") ## On récupère la modélisation de pays.csv et on la stocke dans tablePays
tableVilles=charger_table("villes.csv") ## On récupère la modalisation de villes.csv et on la stocke dans tableVilles
tableLangues=charger_table("langues.csv") ## On récupère la modalisation de langues.csv et on la stocke dans tableLangues
#print(tableVilles[0]) ## A compléter

def afficher_table(*args): ## On crée la fonction afficher_table qui prend en argument une table et potentiellement le début de la table affichée, par défaut 0 et la fin de la table, par défaut None. Il permettra de créer une nouvelle table, plus petite que la précédente qui commence à la ligne args[1] et finit à la ligne args[2] si spécifiés

    Table=args[0] ## On récupère dans les arguments la table passée, il s'agit du premier argument
    if len(args)==1: ## S'il n'y a qu'un argument (la table) on définit le début comme étant 0 et la fin, la longueur de la table, ce qui correspond au fait que quand aucun début et aucune fin n'est renseignée, la table s'affiche en entier
        debut=0 ## On met la variable début à 0
        fin=len(Table) ## On met la variable fin à la longueur de la table
    else: ## En revanche, si l'on dispose des arguments de début et fin, on va les renseigner dans les variables début et fin afin de n'afficher que la partie de la table voulue
        debut=args[1] ## De ce fait début est égal au deuxième argument donné
        fin=args[2] ## Et la fin est le troisième argument donné lors de l'appel de la fonction

    Table=Table[debut:fin] # On modifie la table pour que la nouvelle table ne contienne que la partie demandée

    if len(Table)==0: ## Si jamais la table ne contient pas d'élément (que sa longueur est égale à 0), on va retourner qu'il est impossible de l'afficher car elle ne contient pas d'arguments
        print("aucune valeur dans ce fichier") ## On affiche l'erreur

    NbColonnes=len(Table[0])  # je cherche le nombres de valeurs contenue dans un tuple de la Table
    ValeursMax=[0]*NbColonnes # je définis une liste contenant la longueur maximale d'un 'mot' pour
                              # chaque colonne de la table
    for elt in Table: ## Pour chaque element dans la table,
        for j in range(len(ValeursMax)): ## On va itérer
            if len(elt[j])>ValeursMax[j]: ## et si la longueur de l'élément est supérieure à la longueur max stockée dans la liste ValeursMax,
                ValeursMax[j]=len(elt[j]) ## on modifie la longueur max de la colonne qui est contenue dans un élément de la liste ValeursMax

    forme="  "  #je définis la forme d'une ligne
    for elt in ValeursMax: ## Pour chaque élément de la valeur max,
        forme+="|{:"+str(elt)+"}" ## On va ajouter à la forme de la ligne ce mot, comme il s'agit du mot de longueur maximal, les autres mots rentreront
    forme+="|" ## On ferme la colonne


    for val in Table: ## Pour toutes les valeurs de la table
        trait="  " ## On va créer le trait qui sépare des valeurs précédentes
        for elt in ValeursMax:
            trait+="+"+"-"*elt
        trait+="+"
        print(trait) ## Pour chaque valeur, on print un trait de séparation avec la valeur d'avant
        print (forme.format(*val)) ## et on print la forme définie précédemment en remplacant le mot par l'élément correspondant
    print(trait) ## On print un trait pour fermer le tableau

# afficher_table(tableVilles,0,3) ## Trois lignes sont affichées

def projection_table(TableTuple,*colonnes):  ## La fonction projection_table prend en argument un tuple qui contient la table que l'on veut projeter, et un intervalle des lignes que l'on veut projeter. les arguments colonnes permettent à la fonction de renvoyer une liste de tuples qui contiennent les valeurs des lignes spécifiées pour les colonnes spécifiées.

    if len(TableTuple)==1: ## Si l'on a que renseigner le nom de la table dans table tuples, cela veut dire que l'on veut projeter toute la table
        Table=TableTuple[0]
        TableTuple=(Table,0,len(Table))


    Table=TableTuple[0][TableTuple[1]:TableTuple[2]]  # on extrait les lignes de la table qui nous interesse

    newTable=[] ## On crée une variable nouvelle table qui sera retournée, elle va contenir les tuples des valeurs qui nous intéresse

    for elt in Table: ## Pour chaque colonne, on va remplir un tuple qui contient les valeurs des colonnes qui nous intéressent
        liste=[]
        for col in colonnes:
            liste.append(elt[col])
        liste=tuple(liste)
        newTable.append(liste) ## On append chaque tuples dans la nouvelle table



    return(newTable) ## On renvoie la nouvelle table
# print(projection_table((tableVilles,0,10),1))
#afficher_table(projection_table((tableVilles,0,10),1,3))

def produit_cartesien(Table1,Table2):

    newTable=[] ## Onn déclare la nouvelle table

    for i in range(len(Table1)): ## Pour la longueur de Table1 (nombre de tuples)
        for j in range(len(Table2)): ## Pour la longueur de Table2 (nombre de tuples)
            newTable.append(tuple(list(Table1[i])+list(Table2[j]))) ## On ajoute l'élément i de Table1 à l'élément j de Table2 transformés chacun en liste et on les transforme dans un tuple

    return(newTable) ## On renvoie la nouvelle table


def join(Table,colonne_A,colonne_B):#on ne prend que les lignes de Table qui ont la même valeur en colonne A et en colonne B

    newTable=[] ## On déclare newTable, une nouvelle liste

    for elt in Table : ## Pour chaque element de Table
        if elt[colonne_A]==elt[colonne_B]: ## Si c'est la même valeur dans les colonnes A et B
            newTable.append(elt) ## On ajoute l'element en commun

    return(newTable) ## On renvoie la Table des éléments en commun


                                               ################################################################################
                                               #                                  exercices                                   #
                                               ################################################################################





def exo1(tableVilles,lettres): ##On renvoie la liste des villes dont le nom commence par lettres
    tableProjection=projection_table((tableVilles,0,len(tableVilles)),1) ## On déclare tableProjection comme une table des noms de ville
    """
    newTable=[] ## On crée une nouvelle liste
    for i in range(len(tableProjection)): ## Pour i allant de 0 à la longueur de tableProjection-1
        if str.upper(tableProjection[i][0][0:len(lettres)])==lettres: ## Si les premieres lettres de l'element i majuscules sont equivalentes a lettres
            newTable.append(tableProjection[i],) ## On ajoute le nom de la ville
    return newTable ## On retourne la liste des noms des villes qui commencent par lettres
    """
    newTable = [tableProjection[i] for i in range(len(tableProjection)) if tableProjection[i][0][0:len(lettres)].upper() == lettres]
    return(newTable) ## On retourne la liste des noms des villes qui commencent par lettres
#afficher_table(exo1(tableVilles,'PA'),0,10)
#print(len(exo1(tableVilles,'PA')))

################################################################################



def exo2(tablePays): ## On veut relever tout les pays d'Amerique du sud
    tableProjection=projection_table((tablePays,0,len(tablePays)),1,2) ## On récupère les colonnes pays et continent du tablePays
    """
    newTable=[]
    for i in range(len(tableProjection)):
        if tableProjection[i][1]=="South America": ## Pour chaque pays, si le continent et South America, on l'append dans newTable
            newTable.append((tableProjection[i][0],))
    """
    newTable = [tableProjection[i] for i in range(len(tableProjection)) if tableProjection[i][1] == "South America"]
    
    return newTable ## On retourne newTable, qui contient à présent tout les pays de South America
    
afficher_table(exo2(tablePays),0,10)
print(len(exo2(tablePays)))

################################################################################

def exo3(tableVilles,tablePays):
    T1=projection_table((tableVilles,0,len(tableVilles)),1,2) ## On déclare T1 comme une table contenant toutes les lignes de tableVilles mais seulement les colonnes 1 et 2, c'est-a-dire  le nom de la ville et le code du pays
    
    
    T2=[] ## On déclare T2, une table vide pour l'instant
    for elt in T1: ## Pour chaque element de T1:
        if str.upper(elt[0][0:len('PA')])=="PA": ## Si le nom de la ville commence par 'PA'
            T2.append(elt,) ## On ajoute l'element dans T2

    T3=projection_table((tablePays,0,len(tablePays)),0,2) ## On recupere la table des pays contenant toutes les lignes mais uniquement les colonnes 0 et 2, c'est-a-dire les codes et les continents
    T4=[] ## On déclare une nouvelle table  T4
                     
    for elt in T3: ## Pour chaque element de T3:
        if elt[1]=='Europe': ## Si le pays est en Europe:
            T4.append(elt,) ## On l'ajoute à T4
                     
    T5=produit_cartesien(T2,T4) ## On
    T6=join(T5,1,2)
    T7=projection_table((T6,0,len(T6)),0)
    return T7

#afficher_table(exo3(tableVilles,tablePays),0,10)
# print(len(exo3(tableVilles,tablePays)))                     


################################################################################


def exo4(tableVilles,tablePays):
    T1=projection_table((tableVilles,0,len(tableVilles)),1,2,4) ## On déclare T1 comme une table contenant toutes les lignes de tableVilles mais seulement les colonnes 1 et 2, c'est-a-dire  le nom de la ville et le code du pays
    
    
    T2=[] ## On déclare T2, une table vide pour l'instant
    for elt in T1: ## Pour chaque element de T1:
        if int(elt[2]) > 100000: ## Si la ville contient plus de 100000 habitants
            T2.append(elt,) ## On ajoute l'element dans T2

    T3=projection_table((tablePays,0,len(tablePays)),0,2) ## On recupere la table des pays contenant toutes les lignes mais uniquement les colonnes 0 et 2, c'est-a-dire les codes et les continents
    T4=[] ## On déclare une nouvelle table  T4
                     
    for elt in T3: ## Pour chaque element de T3:
        if elt[1]=='Europe': ## Si le pays est en Europe
            T4.append(elt,) ## On l'ajoute a T4
                     
    T5=produit_cartesien(T2,T4) ## 
    T6=join(T5,1,3)
    T7=projection_table((T6,0,len(T6)),0)
    return T7

#afficher_table(exo4(tableVilles,tablePays),0,10)
#print(len(exo4(tableVilles,tablePays))) 


################################################################################


def exo5_6(colonne):
    T1 = projection_table((tablePays, 0, len(tablePays)), colonne)
    T2 = list(set(T1)) ## On utilise un set puisqu'il ne peut contenir qu'une fois chaque valeur
    return(T2)

#print(len(exo5_6(11)))


################################################################################

#print(len(exo5_6(1)))






                                               
