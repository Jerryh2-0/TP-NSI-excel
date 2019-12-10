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



## Définition des erreurs

class MustBeAnOperator(Exception):
    def __init__(self):
        pass

## Fonctions réutilisables

def condition(table, *args): ## On définit une fonction nommée condition qui va nous permettre de trier un tableau en gardant les lignes qui respectent les conditions voulues. Les conditions sont des tuples constituées de trois éléments, la colonne, l'opérateur conditionnel, la valeur testée et le type de variable (int ou str)
    ##avec args une liste de tuples de longueurs 4 sous la forme (colonne, operateur, valeur)
    for condition in args:
        # print(condition)
        # afficher_table(table, 0, 10)
        """
        if condition[1]=="==": table = list(filter(lambda elt : elt == condition[2] , (list(map(lambda elt : float(elt), table[condition[0]])) if (type(condition[2])==float or type(condition[2])==int) else table[condition[0]])))
        elif condition[1]==">=": table = list(filter(lambda elt : elt >= condition[2], (list(map(lambda elt : float(elt), table[condition[0]])) if (type(condition[2])==float or type(condition[2])==int) else table[condition[0]])))
        elif condition[1]=="<=": table = list(filter(lambda elt : elt <= condition[2], (list(map(lambda elt : float(elt), table[condition[0]])) if (type(condition[2])==float or type(condition[2])==int) else table[condition[0]])))
        elif condition[1]==">": table = list(filter(lambda elt : elt > condition[2], (list(map(lambda elt : float(elt), table[condition[0]])) if (type(condition[2])==float or type(condition[2])==int) else table[condition[0]])))
        elif condition[1]=="<": table = list(filter(lambda elt : elt < condition[2], (list(map(lambda elt : float(elt), table[condition[0]])) if (type(condition[2])==float or type(condition[2])==int) else table[condition[0]])))
        else: raise MustBeAnOperator('The second argument of the tuples must be a conditional operator')
        """
        if condition[1]=="==": table = list(filter(lambda elt : float(elt[condition[0]]) == condition[2] ,  table)) if (type(condition[2])==float or type(condition[2])==int) else list(filter(lambda elt : elt[condition[0]] == condition[2] ,  table))
        elif condition[1]==">=": table = list(filter(lambda elt : float(elt[condition[0]]) >= condition[2], table)) if (type(condition[2])==float or type(condition[2])==int) else list(filter(lambda elt : elt[condition[0]] >= condition[2] ,  table))
        elif condition[1]=="<=": table = list(filter(lambda elt : float(elt[condition[0]]) <= condition[2], table)) if (type(condition[2])==float or type(condition[2])==int) else list(filter(lambda elt : elt[condition[0]] <= condition[2] ,  table))
        elif condition[1]==">": table = list(filter(lambda elt : float(elt[condition[0]]) > condition[2], table)) if (type(condition[2])==float or type(condition[2])==int) else list(filter(lambda elt : elt[condition[0]] > condition[2] ,  table))
        elif condition[1]=="<": table = list(filter(lambda elt : float(elt[condition[0]]) < condition[2], table)) if (type(condition[2])==float or type(condition[2])==int) else list(filter(lambda elt : elt[condition[0]] < condition[2] ,  table))
        else: raise MustBeAnOperator('The second argument of the tuples must be a conditional operator')
        # afficher_table(table, 0, 10)
    return table


################################################################################


def exo1(tableVilles, lettres, proj): ##On renvoie la liste des villes dont le nom commence par lettres
    tableProjection = projection_table((tableVilles,0,len(tableVilles)),1) if proj==1 else tableVilles ## On déclare tableProjection comme une table des noms de ville si on veut faire une projection, sinon, on donne comme valeur la table des Villes données en argument
    newTable = [elt for elt in tableProjection if elt[0][0:len(lettres)].upper() == lettres] ## On récupère dans newTable les villes dont le nom commence par lettres
    return(newTable) ## On retourne la liste des noms des villes qui commencent par lettres

# afficher_table(exo1(tableVilles,'PA', 1),0,10)
# print(len(exo1(tableVilles,'PA', 1)))


################################################################################


def exo2(tablePays, continent, proj): ## On veut relever tout les pays d'Amerique du sud, on donne l'argument continent qui sera un string, ainsi cette fonction pourra fonctionner pour tout continent
    tableProjection = projection_table((tablePays,0,len(tablePays)),1,2) if proj==1 else tablePays ## On récupère les colonnes pays et continent du tablePays si proj est 1 sinon, on y assigne la table demandé en argument de la fonction
    newTable = [tableProjection[i] for i in range(len(tableProjection)) if tableProjection[i][1] == continent] ## On récupère dans tableProjection les noms des pays se trouvant sur le continant donné en argument
    return newTable ## On retourne newTable, qui contient à présent tout les pays du continent continent
    
# afficher_table(exo2(tablePays, "South America", 1),0,10)
# print(len(exo2(tablePays, "South America", 1)))


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
# print(len(exo3(tableVilles,tablePays)))                     


################################################################################


def exo4(tableVilles,tablePays):
    T1=projection_table((tableVilles,0,len(tableVilles)),1,2,4) ## On déclare T1 comme une table contenant toutes les lignes de tableVilles mais seulement les colonnes 1 et 2, c'est-a-dire  le nom de la ville et le code du pays
    """
    T2=[] ## On déclare T2, une table vide pour l'instant
    for elt in T1: ## Pour chaque element de T1:
        if int(elt[2]) > 100000: ## Si la ville contient plus de 100000 habitants
            T2.append(elt,) ## On ajoute l'element dans T2
    """
    # afficher_table(T1, 0, 10)
    T2 = condition(T1, (2, ">", 100000))
    T3=projection_table((tablePays,0,len(tablePays)),0,2) ## On recupere la table des pays contenant toutes les lignes mais uniquement les colonnes 0 et 2, c'est-a-dire les codes et les continents
    """
    T4=[] ## On déclare une nouvelle table  T4
                     
    for elt in T3: ## Pour chaque element de T3:
        if elt[1]=='Europe': ## Si le pays est en Europe
            T4.append(elt,) ## On l'ajoute a T4
    """
    T4 = condition(T3, (1, "==", "Europe"))              
    T5=produit_cartesien(T2,T4) ## 
    T6=join(T5,1,3)
    T7=projection_table((T6,0,len(T6)),0)
    return T7

afficher_table(exo4(tableVilles,tablePays),0,10)
print(len(exo4(tableVilles,tablePays))) 


################################################################################


def exo5_6(colonne):
    T1 = projection_table((tablePays, 0, len(tablePays)), colonne)
    T2 = list(set(T1)) ## On utilise un set puisqu'il ne peut contenir qu'une fois chaque valeur
    return(T2)

# print(len(exo5_6(11)))


################################################################################


# print(len(exo5_6(1)))


################################################################################


def exo7():
    T1 = projection_table((tablePays, 0, len(tablePays)), 0, 1)
    T3 = projection_table((tableLangues, 0, len(tableLangues)), 0, 1)
    T4 = list(filter(lambda elt : elt[1] == "French", T3))
    T5 = produit_cartesien(T1, T4)
    T6 = join(T5, 0, 2)
    T7 = projection_table((T6, 0, len(T6)), 1)
    return(T7)

# afficher_table((exo7()), 0, 10)
# print(len(exo7()))


################################################################################


def exo8():
    T1 = projection_table((tablePays, 0, len(tablePays)), 0, 1)
    T3 = projection_table((tableLangues, 0, len(tableLangues)), 0, 1, 2)
    T4 = list(filter(lambda elt : elt[1] == "French" and elt[2] == "T", T3))
    T5 = produit_cartesien(T1, T4)
    T6 = join(T5, 0, 2)
    T7 = projection_table((T6, 0, len(T6)), 1)
    return T7
                                               
# afficher_table((exo8()), 0, 10)
# print(len(exo8()))


################################################################################


def exo9():
    T1 = projection_table((tableVilles, 0, len(tableVilles)), 1, 2, 4)
    T2 = list(filter(lambda elt : int(elt[2]) < 100000, T1))
    T3 = projection_table((tablePays, 0, len(tablePays)), 0, 2)
    T4 = list(filter(lambda elt : elt[1] == "Africa", T3))
    T5 = produit_cartesien(T2, T4)
    T6 = join(T5, 1, 3)
    T7 = projection_table((T6, 0, len(T6)), 0, 1)
    T8 = projection_table((tableLangues, 0, len(tableLangues)), 0, 1, 2)
    T9 = list(filter(lambda elt : elt[1] == "French" and elt[2] == "T", T8))
    T10 = produit_cartesien(T7, T9)
    T11 = join(T10, 1, 2)
    T12 = projection_table((T11, 0, len(T11)), 0)
    return T12

# afficher_table((exo9()), 0, 10)
# print(len(exo9()))


################################################################################


def exo10():
    T1 = projection_table((tablePays, 0, len(tablePays)), 1, 3, 6, 11)
    T3 = list(filter(lambda elt : elt[1] == "South America" and int(elt[2]) > 10000000 and elt[3] == "Republic", T1))
    T4 = projection_table((T3, 0, len(T3)), 0)
    return T4

# afficher_table((exo10()), 0, 10)
# print(len(exo10()))


################################################################################


def exo11():
    T1 = projection_table((tableVilles, 0, len(tableVilles)), 1, 2, 4)
    T2 = list(filter(lambda elt : int(elt[2]) > 100000, T1))
    T3 = projection_table((tablePays, 0, len(tablePays)), 0, 2)
    T4 = list(filter(lambda elt : elt[1] == "North America", T3))
    T5 = produit_cartesien(T2, T4)
    T6 = join(T5, 1, 3)
    T7 = projection_table((T6, 0, len(T6)), 0, 1)
    T8 = projection_table((tableLangues, 0, len(tableLangues)), 0, 1)
    T9 = list(filter(lambda elt : elt[1] == "Spanish", T8))
    T10 = produit_cartesien(T7, T9)
    T11 = join(T10, 1, 2)
    T12 = projection_table((T11, 0, len(T11)), 0)
    return T12

# afficher_table((exo11()), 0, 10)
# print(len(exo11()))


################################################################################


def exo12():
    T1 = projection_table((tablePays, 0, len(tablePays)), 2, 4)
    T2 = list(filter(lambda elt : elt[0] == "Europe", T1))
    totalArea = 0
    for elt in T2:
        totalArea += float(elt[1])
    return(totalArea)

# print(f'{exo12()} à 0.1 près')


################################################################################


def exo13():
    T1 = projection_table((tablePays, 0, len(tablePays)), 3, 4)
    T2 = list(filter(lambda elt : elt[0] == "Polynesia", T1))
    totalArea = 0
    for elt in T2:
        totalArea += float(elt[1])
    return(totalArea)

# print(f'{exo13()} à 0.1 près')


################################################################################


def exo14():
    T1 = projection_table((tablePays, 0, len(tablePays)), 2, 4)
    T2 = list(filter(lambda elt : elt[0] == "Oceania" and float(elt[1])>10000, T1))
    return(len(T2))

# print(exo14())
