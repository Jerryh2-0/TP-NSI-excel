# -*- coding: utf-8 -*-

import codecs
import pprint
import csv

def charger_table(nom):
    csvfile = codecs.open(nom, encoding='utf-8')
    lecteurcsv = csv.reader(csvfile,delimiter=';')

    tab=[]
    for ligne in lecteurcsv:
        tab.append(tuple(ligne))
    return tab

tablePays=charger_table("pays.csv")
tableVilles=charger_table("villes.csv")
tableLangues=charger_table("langues.csv")
#print(tableVilles[0])

def afficher_table(*args):

    Table=args[0]
    if len(args)==1:
        debut=0
        fin=len(Table)
    else:
        debut=args[1]
        fin=args[2]

    Table=Table[debut:fin] # correspond aux lignes de la Table que l'on veut afficher

    if len(Table)==0:
        print("aucune valeur dans ce fichier")

    NbColonnes=len(Table[0])  # je cherche le nombres de valeurs contenue dans un tuple de la Table
    ValeursMax=[0]*NbColonnes # je définis une liste contenant la longueur maximale d'un 'mot' pour
                              # chaque colonne de la table
    for elt in Table:
        for j in range(len(ValeursMax)):
            if len(elt[j])>ValeursMax[j]:
                ValeursMax[j]=len(elt[j])

    forme="  "  #je définis la forme d'une ligne
    for elt in ValeursMax:
        forme+="|{:"+str(elt)+"}"
    forme+="|"


    for val in Table:
        trait="  "
        for elt in ValeursMax:
            trait+="+"+"-"*elt
        trait+="+"
        print(trait)
        print (forme.format(*val))
    print(trait)

#afficher_table(tableVilles,0,3)

def projection_table(TableTuple,*colonnes):  # TableTuple est un Tuple dont le premier élément est une Table et les autres sont les lignes à prendre en compte

    if len(TableTuple)==1:
        Table=TableTuple[0]
        TableTuple=(Table,0,len(Table))


    Table=TableTuple[0][TableTuple[1]:TableTuple[2]]  # on extrait les lignes de la table qui nous interesse

    newTable=[]

    for elt in Table:
        liste=[]
        for col in colonnes:
            liste.append(elt[col])
        liste=tuple(liste)
        newTable.append(liste)



    return(newTable)
#print(projection_table((tableVilles,0,10),1))
#afficher_table(projection_table((tableVilles,0,10),1,3))

def produit_cartesien(Table1,Table2):

    newTable=[]

    for i in range(len(Table1)):
        for j in range(len(Table2)):
            newTable.append(tuple(list(Table1[i])+list(Table2[j])))

    return(newTable)


def join(Table,colonne_A,colonne_B):#on ne prend que les lignes de Table qui ont la même valeur en colonne A et en colonne B

    newTable=[]

    for elt in Table :
        if elt[colonne_A]==elt[colonne_B]:
            newTable.append(elt)

    return(newTable)


                                               ################################################################################
                                               #                                  exercices                                   #
                                               ################################################################################





def exo1(tableVilles,lettres):
    tableProjection=projection_table((tableVilles,0,len(tableVilles)),1)
    newTable=[]
    for i in range(len(tableProjection)):
        if str.upper(tableProjection[i][0][0:len(lettres)])==lettres:
            newTable.append(tableProjection[i],)
    return newTable

#afficher_table(exo1(tableVilles,'PA'),0,10)
#print(len(exo1(tableVilles,'PA')))

################################################################################



def exo2(tablePays):
    tableProjection=projection_table((tablePays,0,len(tablePays)),1,2)
    
    newTable=[]
    for i in range(len(tableProjection)):
        if tableProjection[i][1]=="South America":
            newTable.append((tableProjection[i][0],))
    return newTable
    
#afficher_table(exo2(tablePays),0,10)


################################################################################

def exo3(tableVilles,tablePays):
    T1=projection_table((tableVilles,0,len(tableVilles)),1,2)
    
    
    T2=[]
    for elt in T1:
        if str.upper(elt[0][0:len('PA')])=="PA":
            T2.append(elt,)

    T3=projection_table((tablePays,0,len(tablePays)),0,2)
    T4=[]
                     
    for elt in T3:
        if elt[1]=='Europe':
            T4.append(elt,)
                     
    T5=produit_cartesien(T2,T4)
    T6=join(T5,1,2)
    T7=projection_table((T6,0,len(T6)),0)
    return T7

afficher_table(exo3(tableVilles,tablePays),0,10)
print(len(exo3(tableVilles,tablePays)))                     















                                               
