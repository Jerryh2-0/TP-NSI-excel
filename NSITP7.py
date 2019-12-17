# -*- coding: utf-8 -*-

import codecs ## On importe codecs qui permet de lire un fichier en spécifiant l'encondage
import pprint ## On importe ppprint qui permet d'afficher des listes efficacement
import csv ## On importe csv qui permet de lire les fichiers .csv

def charger_table(nom): ## On définit la fonction charger_table qui prend en argument un string, nom et qui ouvre le fichier qui dispose de ce nom
    csvfile = codecs.open(nom, encoding='utf-8') ## On ouvre le fichier avec un encodage utf-8 grâce à codecs
    lecteurcsv = csv.reader(csvfile,delimiter=';') ## On lit le resultat de l'ouverture du fichier à l'aide de la mathode reader de csv
    
    return [tuple(ligne) for ligne in lecteurcsv] ## On renvoie une liste de tuples avec un tuple = une ligne
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



## Définition d'une erreur

class MustBeAnOperator(Exception): ## On créer une classe enfant de Exception qui va donc hériter des propriétés de Exception
    def __init__(self):
        pass

## Fonctions réutilisables

def condition(table, *args): ## On définit une fonction nommée condition qui va nous permettre de trier un tableau en gardant les lignes qui respectent les conditions voulues. Les conditions sont des tuples constituées de trois éléments, la colonne, l'opérateur conditionnel, la valeur testée et le type de variable (int ou str)
    ##avec args une liste de tuples de longueurs 4 sous la forme (colonne, operateur, valeur)
    for condition in args: ## Pour chaque condition représenté par un des tuples
        if condition[1]=="==": table = list(filter(lambda elt : float(elt[condition[0]]) == condition[2] ,  table)) if (type(condition[2])==float or type(condition[2])==int) else list(filter(lambda elt : elt[condition[0]] == condition[2] ,  table)) ## On test pour le str si la valeur donné en argument est un string sinon, on transforme en float
        elif condition[1]=="!=": table = list(filter(lambda elt : float(elt[condition[0]]) != condition[2], table)) if (type(condition[2])==float or type(condition[2])==int) else list(filter(lambda elt : elt[condition[0]] != condition[2] ,  table)) ## On test pour le str si la valeur donné en argument est un string sinon, on transforme en float
        elif condition[1]==">=": table = list(filter(lambda elt : float(elt[condition[0]]) >= condition[2], table)) if (type(condition[2])==float or type(condition[2])==int) else list(filter(lambda elt : elt[condition[0]] >= condition[2] ,  table)) ## On test pour le str si la valeur donné en argument est un string sinon, on transforme en float
        elif condition[1]=="<=": table = list(filter(lambda elt : float(elt[condition[0]]) <= condition[2], table)) if (type(condition[2])==float or type(condition[2])==int) else list(filter(lambda elt : elt[condition[0]] <= condition[2] ,  table)) ## On test pour le str si la valeur donné en argument est un string sinon, on transforme en float
        elif condition[1]==">": table = list(filter(lambda elt : float(elt[condition[0]]) > condition[2], table)) if (type(condition[2])==float or type(condition[2])==int) else list(filter(lambda elt : elt[condition[0]] > condition[2] ,  table)) ## On test pour le str si la valeur donné en argument est un string sinon, on transforme en float
        elif condition[1]=="<": table = list(filter(lambda elt : float(elt[condition[0]]) < condition[2], table)) if (type(condition[2])==float or type(condition[2])==int) else list(filter(lambda elt : elt[condition[0]] < condition[2] ,  table)) ## On test pour le str si la valeur donné en argument est un string sinon, on transforme en float
        else: raise MustBeAnOperator('The second argument of the tuples must be a conditional operator')
        # afficher_table(table, 0, 10)
    return table


################################################################################


def exo1(tableVilles, lettres, proj): ##On renvoie la liste des villes dont le nom commence par lettres
    tableProjection = projection_table((tableVilles,0,len(tableVilles)),1) if proj==1 else tableVilles ## On déclare tableProjection comme une table des noms de ville si on veut faire une projection, sinon, on donne comme valeur la table des Villes données en argument
    newTable = [elt for elt in tableProjection if elt[0][0:len(lettres)].upper() == lettres] ## On récupère dans newTable les villes dont le nom commence par lettres
    return(newTable) ## On retourne la liste des noms des villes qui commencent par lettres

# afficher_table(exo1(tableVilles,'PA', 1),0,10)
# print(len(exo1(tableVilles,'PA', 1)))#70


################################################################################


def exo2(tablePays, continent, proj): ## On veut relever tout les pays d'Amerique du sud, on donne l'argument continent qui sera un string, ainsi cette fonction pourra fonctionner pour tout continent
    tableProjection = projection_table((tablePays,0,len(tablePays)),1,2) if proj==1 else tablePays ## On récupère les colonnes pays et continent du tablePays si proj est 1 sinon, on y assigne la table demandé en argument de la fonction
    newTable = [tableProjection[i] for i in range(len(tableProjection)) if tableProjection[i][1] == continent] ## On récupère dans tableProjection les noms des pays se trouvant sur le continant donné en argument
    return newTable ## On retourne newTable, qui contient à présent tout les pays du continent continent
    
# afficher_table(exo2(tablePays, "South America", 1),0,10)
# print(len(exo2(tablePays, "South America", 1)))#14


################################################################################


def exo3(tableVilles,tablePays):
    T1=projection_table((tableVilles,0,len(tableVilles)),1,2) ## On déclare T1 comme une table contenant toutes les lignes de tableVilles mais seulement les colonnes 1 et 2, c'est-a-dire  le nom de la ville et le code du pays
    T2 = exo1(T1, "PA", 0) ## T2 est la table des villes dont le nom commence par "PA"
    T3=projection_table((tablePays,0,len(tablePays)),0,2) ## On recupere la table des pays contenant toutes les lignes mais uniquement les colonnes 0 et 2, c'est-a-dire les codes et les continents
    T4=exo2(T3, "Europe", 0) ## On déclare une nouvelle table  T4 qui contient les pays d'Europe    
    T5=produit_cartesien(T2,T4) ## On fait le produit cartésien des tableaux T2 et T4, permettant de retrouver les villes qui nous intéressent plus tard
    T6=join(T5,1,2) ## On trie le tableau précédemment obtenu par produit, on garde uniquement les lignes qui ont les mêmes éléments dans les colonne 1 et 2
    T7=projection_table((T6,0,len(T6)),0) ## On récupère seulement la colonne intéressante du tableau T6 c'est à dire les noms des villes d'Europe commençant par pa
    return T7 ## On retourne le tableau T7

# afficher_table(exo3(tableVilles,tablePays),0,10)
# print(len(exo3(tableVilles,tablePays)))#11


################################################################################


def exo4(tableVilles,tablePays): ## On définit la fonction qui va nous retourner les villes de plus de 100000 habitants en europe
    T1=projection_table((tableVilles,0,len(tableVilles)),1,2,4) ## On déclare T1 comme une table contenant toutes les lignes de tableVilles mais seulement les colonnes 1 et 2, c'est-a-dire  le nom de la ville et le code du pays
    # afficher_table(T1, 0, 10)
    T2 = condition(T1, (2, ">", 100000)) ## On ne garde que les villes qui ont plus de 100000 habitants, (nb d'habitant dans la colonne 2)
    T3 = projection_table((tablePays,0,len(tablePays)),0,2) ## On recupere la table des pays contenant toutes les lignes mais uniquement les colonnes 0 et 2, c'est-a-dire les codes et les continents
    T4 = condition(T3, (1, "==", "Europe")) ## On ne garde que les villes qui sont en Europe             
    T5=produit_cartesien(T2,T4) ## On fait le produit cartesien des villes de plus de 100000 et les pays d'Europe
    T7=projection_table((join(T5,1,3),0,len(join(T5,1,3))),0) ## On projete la table des villes de plus de 100000 habitants d'Europe
    return T7 ## On retourne les informations demandées dans l'exercice 4

# afficher_table(exo4(tableVilles,tablePays),0,10)
# print(len(exo4(tableVilles,tablePays)))#711


################################################################################


def exo5_6(colonne): ## On définit la fonction exo5_6 qui prend simplement une colonne (int) d'un tableau et va
    T1 = projection_table((tablePays, 0, len(tablePays)), colonne) ## On projete la table des pays avec uniquement sa colonne precisee en argument
    return list(set(T1)) ## On utilise un set puisqu'il ne peut contenir qu'une fois chaque valeur

# print(len(exo5_6(11)))#37


################################################################################


# print(len(exo5_6(1)))#239


################################################################################


def exo7():
    T1 = projection_table((tablePays, 0, len(tablePays)), 0, 1) ## On garde les colonnes 0 et 1 des pays
    T2 = condition(projection_table((tableLangues, 0, len(tableLangues)), 0, 1), (1, "==", "French")) ## On prend les pays où; le français est parle
    T3 = produit_cartesien(T1, T2) ## On fait le produit cartesien
    T4 = join(T3, 0, 2) ## On garde les valeurs identiques en 0 et 2
    return(projection_table((T4, 0, len(T4)), 1)) ## On renvoie la liste des noms des pays correspondant

# afficher_table((exo7()), 0, 10)
# print(len(exo7()))#25


################################################################################


def exo8():
    T1 = condition(projection_table((tableLangues, 0, len(tableLangues)), 0, 1, 2), (1, "==", "French"), (2, "==", "T")) ## On prend les pays où le français est la langue officielle
    T2 = produit_cartesien(projection_table((tablePays, 0, len(tablePays)), 0, 1), T1) ## On va chercher les pays correspondant
    T3 = join(T2, 0, 2) ## On garde les pays où le français est la langue officielle
    return projection_table((T3, 0, len(T3)), 1) ## On renvoie les noms des pays
                                               
# afficher_table((exo8()), 0, 10)
# print(len(exo8()))#18


################################################################################


def exo9():
    T1 = condition(projection_table((tableVilles, 0, len(tableVilles)), 1, 2, 4), (2, "<", 100000)) ## On recupere la liste des villes de moins de 100000 habitants
    T2 = condition(projection_table((tablePays, 0, len(tablePays)), 0, 2), (1, "==", "Africa")) ## On recupere la liste des pays d'Afrique
    T3 = join(produit_cartesien(T1, T2), 1, 3) ## On fait le produit cartesien des deux tables
    T4 = projection_table((T3, 0, len(T3)), 0, 1) ## On ne garde que les colonnes 0 et 1
    T5 = condition(projection_table((tableLangues, 0, len(tableLangues)), 0, 1, 2), (1, "==", "French"), (2, "==", "T")) ## On recupere la liste des pays où le français est la langue officielle
    T6 = join(produit_cartesien(T4, T5), 1, 2) ## On fait le produit cartesien
    return projection_table((T6, 0, len(T6)), 0) ## On renvoie uniquement les villes d'Afrique où la langue officielle est le français

# afficher_table((exo9()), 0, 10)
# print(len(exo9()))#3


################################################################################


def exo10():
    T1 = condition(projection_table((tablePays, 0, len(tablePays)), 1, 3, 6, 11), (1, "==", "South America"), (2, ">", 10000000), (3, "==", "Republic")) ## On recupere la liste des pays d'Amerique du Sud de plus de 10 millions d'habitants ayant une republique comme regime politique
    return projection_table((T1, 0, len(T1)), 0) ## On renvoie la liste de leurs noms

# afficher_table((exo10()), 0, 10)
# print(len(exo10()))#4


################################################################################


def exo11():
    T1 = condition(projection_table((tableVilles, 0, len(tableVilles)), 1, 2, 4), (2, ">", 100000)) ## On recupere la liste des villes de plus de 100000 habitants
    T2 = condition(projection_table((tablePays, 0, len(tablePays)), 0, 2), (1, "==", "North America")) ## On recupere les pays d'Amerique du Nord
    T3 = join(produit_cartesien(T1, T2), 1, 3) ## On garde les valeurs identiques en 1 et 3
    T4 = projection_table((T3, 0, len(T3)), 0, 1) ## On ne garde que les colonnes 0 et 1
    T5 = condition(projection_table((tableLangues, 0, len(tableLangues)), 0, 1), (1, "==", "Spanish")) ## On recupere la liste des pays ou l'espagnol est pratique
    T6 = join(produit_cartesien(T4, T5), 1, 2) ## On ne garde que les valeurs identiques en 1 et 2
    return projection_table((T6, 0, len(T6)), 0) ## On renvoie la liste des noms des villes

# afficher_table((exo11()), 0, 10)
# print(len(exo11()))#483


################################################################################


def exo12():
    T2 = condition(projection_table((tablePays, 0, len(tablePays)), 2, 4), (0, "==", "Europe")) ## On recupere les pays d'Europe
    totalArea = 0 ## On definit totalArea comme aire totale de l'Europe
    for elt in T2: ## Pour chaque element de T2
        totalArea += float(elt[1]) ## On ajoute son aire
    return(totalArea) ## On renvoie l'aire de l'Europe

# print(f'{exo12()} à 0.1 près')#23049133.9


################################################################################


def exo13():
    totalArea = 0 ## On declare totalArea comme l'aire totale de la Polynesie
    for elt in condition(projection_table((tablePays, 0, len(tablePays)), 3, 4), (0, "==", "Polynesia")): ## Pour chaque element de la liste des pays de Polynesie
        totalArea += float(elt[1]) ## On ajoute son aire à la variable
    return(totalArea) ## On renvoie l'aire totale de Polynesie

# print(f'{exo13()} à 0.1 près')#8463.0


################################################################################


def exo14():
    return(len(condition(projection_table((tablePays, 0, len(tablePays)), 2, 4), (0, "==", "Oceania"), (1, ">", 10000)))) ## On renvoie les pays d'Oceanie de plus de 10000 habitants

# print(exo14())#7

#########################################################################################################

def exo_15():
    T1 = condition(projection_table((tablePays, 0, len(tablePays)), 0, 3), (1, "==", "Eastern Europe")) ## On recupere la liste des pays d'Europe de l'Est
    T2 = projection_table((T1, 0, len(T1)), 0) ## On ne garde que les noms de ces pays
    T3 = list(filter(lambda elt: (elt[0],) in T2 and elt[2] == "T", projection_table((tableLangues, 0, len(tableLangues)), 0, 1, 2))) ## On recupere la liste des langues officielles d'Europe de l'Est
    T4 = list(set(projection_table((T3, 0, len(T3)), 1))) ## On ne garde que les noms des langues et on supprime les doublons
    return T4 ## On renvoie la liste de ces noms

# afficher_table(exo_15, 0, 10)
# [print(elt) for elt in exo_15()]
# print(len(exo_15()))#10

def exo_16():
    T1 = condition(projection_table((tablePays, 0, len(tablePays)), 2, 6), (0, "==", "Asia")) ## On recupere la liste des pays d'Asie
    totalPop = 0 ## On declare totalPop comme population totale en Asie
    for elt in T1:
        totalPop += int(elt[1])
    return totalPop/len(T1)

# print(exo_16())#72 647 562.74509804

def exo_17():
    T1 = condition(projection_table((tablePays, 0, len(tablePays)), 0, 2), (1, "==", "Asia"))
    T2 = projection_table((T1, 0, len(T1)), 0)
    T3 = list(filter(lambda elt: (elt[0], ) in T2, projection_table((tableVilles, 0, len(tableVilles)), 2, 4)))
    totalPop = 0
    for elt in projection_table((T3, 0, len(T3)), 1):
        totalPop += int(elt[0])
    return totalPop/len(T3)

# print(exo_17())#395 019

def exo_18():
    T1 = condition(projection_table((tablePays, 0, len(tablePays)), 2, 13), (0, "==", "Europe"))
    T2 = projection_table((T1, 0, len(T1)), 1)
    T3 = list(filter(lambda elt: (elt[0],) in T2 , projection_table((tableVilles, 0, len(tableVilles)), 0, 1)))
    T4 = sorted(projection_table((T3, 0, len(T3)), 1), key=lambda elt : elt[0])  
    return T4

# afficher_table(exo_18(), 0, 10)
# print(len(exo_18()))#46

def exo_19():
    T1 = condition(projection_table((tablePays, 0, len(tablePays)), 0, 2, 13), (1, "==", "Africa"))
    T2 = condition(projection_table((tableVilles, 0, len(tableVilles)), 0, 4), (1, ">=", 3000000))
    T3 = list(filter(lambda elt : (elt[1],) in projection_table((T2, 0, len(T2)), 0), projection_table((T1, 0, len(T1)), 0, 2)))
    T4 = list(filter(lambda elt : (elt[1],) in projection_table((T3, 0, len(T3)), 0), projection_table((tableVilles, 0, len(tableVilles)), 1, 2)))
    return T4

# afficher_table(exo_19(), 0, 10)
# print(len(exo_19()))#37

def exo_20():
    T1 = condition(projection_table((tablePays, 0, len(tablePays)), 0, 2, 5), (1, "==", "North America"), (2, "!=", "NULL"), (2, "<", 1912))
    T2 = list(filter(lambda elt : (elt[0],) in projection_table((T1, 0, len(T1)), 0), projection_table((tableVilles, 0, len(tableVilles)), 2)))
    numOfOccur = {}
    for i in T2:
        if i[0] in numOfOccur.keys():
            numOfOccur[i[0]] += 1
        else:
            numOfOccur[i[0]] = 1
    T3 = list(filter(lambda elt : numOfOccur[elt[0]]>49, T1))
    T4 = condition(projection_table((tableLangues, 0, len(tableLangues)), 0, 1), (1, "==", "Portuguese"))
    T5 = list(filter(lambda elt : (elt[0],) in projection_table((T4, 0, len(T4)), 0), T3))
    return T5

# afficher_table(exo_20(), 0, 10)
# print(len(exo_20()))#1

def exo_21():
    T1 = projection_table((tableVilles, 0, len(tableVilles)), 2, 4)
    paysVillesPasGrandes = []
    paysAyantVilles = set()
    for elt in T1:
        if not(int(elt[1])>100000):
            paysVillesPasGrandes.append(elt[0])
        paysAyantVilles.add(elt[0])
    T2 = list(filter(lambda elt : not(elt[0] in paysVillesPasGrandes) and elt[0] in paysAyantVilles, projection_table((tablePays, 0, len(tablePays)), 0, 1)))
    return T2

# afficher_table(exo_21(), 0, 10)
# print(len(exo_21()))#77

def exo_22():
    T1 = projection_table((tableVilles, 0, len(tableVilles)), 2, 4)
    T2 = condition(projection_table((tableVilles, 0, len(tableVilles)), 2, 4), (0, "==", "NPL"))
    nepalVilles = sorted(T2, key=lambda elt : int(elt[1]), reverse=True)
    taille = int(nepalVilles[0][1])
    paysVillesPasGrandes = []
    paysAyantVilles = set()
    for elt in T1:
        if int(elt[1]) <= taille:
            paysVillesPasGrandes.append(elt[0])
        paysAyantVilles.add(elt[0])
    T2 = list(filter(lambda elt : not(elt[0] in paysVillesPasGrandes) and elt[0] in paysAyantVilles, projection_table((tablePays, 0, len(tablePays)), 0, 1)))
    return T2

# afficher_table(exo_22(), 0, 10)
# print(len(exo_22()))#9

def exo_23():
    T1 = condition(projection_table((tableLangues, 0, len(tableLangues)), 0, 1), (1, "==", "French"))
    paysFrancophones = projection_table((T1, 0, len(T1)), 0)
    T2 = condition(projection_table((tableLangues, 0, len(tableLangues)), 0, 1), (1, "==", "English"))
    paysAnglophones = projection_table((T2, 0, len(T2)), 0)
    T3 = list(filter(lambda elt : not(elt in paysAnglophones), paysFrancophones))
    T4 = list(filter(lambda elt : (elt[0],) in T3, projection_table((tablePays, 0, len(tablePays)), 0, 1)))
    return T3
    # return projection_table((T4, 0, len(T4)), 1)

afficher_table(exo_23())
print(len(exo_23()))#19#20

def exo_24():
    T1 = projection_table((tableVilles, 0, len(tableVilles)), 2)
    T2 = list(set(list(T1)))
    paysAvecVilleDansData = [elt[0] for elt in T2]
    T3 = projection_table((tablePays, 0, len(tablePays)), 0, 1)
    T4 = list(filter(lambda elt : elt[0] in paysAvecVilleDansData, T3))
    return projection_table((T4, 0, len(T4)), 1)

# afficher_table(exo_24(), 0, 10)
# print(len(exo_24()))#232

def exo_25():
    T1 = projection_table((tableLangues, 0, len(tableLangues)), 0)
    T2 = list(set(list(T1)))
    paysAvecLangueDansData = [elt[0] for elt in T2]
    T3 = projection_table((tablePays, 0, len(tablePays)), 0, 1)
    T4 = list(filter(lambda elt : not(elt[0] in paysAvecLangueDansData), T3))
    return projection_table((T4, 0, len(T4)), 1)

# afficher_table(exo_25(), 0, 10)
# print(len(exo_25()))#6

def exo_26():
    T1 = projection_table((tableVilles, 0, len(tableVilles)), 2, 4)
    sommeParPays = {}
    for elt in T1:
        if elt[0] in sommeParPays.keys():
            sommeParPays[elt[0]] += int(elt[1])
        else:
            sommeParPays[elt[0]] = int(elt[1])
    T2 = projection_table((tablePays, 0, len(tablePays)), 0, 1)
    T3 = list(filter(lambda elt : sommeParPays[elt[0]] >= 10000000 if elt[0] in sommeParPays.keys() else False, T2))
    return projection_table((T3, 0, len(T3)), 1)
# afficher_table(exo_26(), 0, 10)
# print(len(exo_26()))#30

def exo_27():
    T1 = condition(projection_table((tablePays, 0, len(tablePays)), 1, 2, 7), (1, "==", "Asia"))
    T2 = sorted(T1, key=lambda elt : float(elt[2]))
    return T2[0][0]

# print(exo_27())#Afghanistan

def exo_28():
    T1 = projection_table((tableLangues, 0, len(tableLangues)), 0)
    nombreLangues = {}
    for elt in T1:
        if elt[0] in nombreLangues.keys(): nombreLangues[elt[0]] += 1
        else: nombreLangues[elt[0]] = 1
    T2 = list(filter(lambda elt : nombreLangues[elt[0]] >= 3, T1))
    paysAmerique = condition(projection_table((tablePays, 0, len(tablePays)), 1, 2, 7), (1, "==", "South America"), (2, "!=", "NULL"))
    paysAmerique = sorted(paysAmerique, key=lambda elt : float(elt[2]), reverse=True)
    esperanceMax = paysAmerique[0][2]
    T3 = condition(projection_table((tablePays, 0, len(tablePays)), 0, 1, 7), (2, ">=", esperanceMax))
    T4 = list(filter(lambda elt : (elt[0],) in T2  and (elt[1],) in exo8(), T3))
    T5 = list(filter(lambda elt : (elt[1],) in projection_table((T4, 0, len(T4)), 0), projection_table((tableVilles, 0, len(tableVilles)), 1, 2)))
    return projection_table((T5, 0, len(T5)), 0)

# afficher_table(exo_28(), 0, 10)
# print(len(exo_28()))#106#+100