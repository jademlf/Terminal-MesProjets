def creer_pile_vide():
    """création de la pile vide"""
    return []

def est_vide(pile):
    """teste si pile est vide et renvoie le booléen obtenu."""
    return (pile == [])

def taille (pile):
    """Renvoie le nombre d'élément de la pile"""
    return len(pile)


def empiler(pile,e):
    """empile l'élément x sur la pile p
        pile.append(e)
        """
    pile[len(pile):] = [e]# on empile

def depiler(pile):
    """depile l'élément x sur la pile pile
    pile.pop()"""
    if est_vide(pile):
        return print("la pile est déjà vide") 
    else:
        del pile[-1]# on depile

def sommet(pile):
    """renvoie le sommet de la pile"""
    return pile[-1]

def enfiler(e,file):
    """file.append(e)"""
    file[len(file):] = [e]

def defiler(file):
    """return file.pop(0)"""
    del file[0]

def longeur(file):
    """Renvoie le nombre d'élément de la file"""
    return len(file)




# def parcours_largeur(G, s):
#     f = []
#     f.append(s)
#     decouverts = {s}                                        # ou marquer s comme découvert
#     while not(est_vide(f)):
#         decouverts = defiler(f)
#         
#         for v in voisins(s):
#                 si v n’est pas dans découverts :
#                     ajouter v à découverts                   # ou marquer v comme découvert
#                     enfiler(f, v)



def BFS(G,x):
    file = []
    sortie = []
    marque = [False]*len(G)
    print(marque)
    marque[x] = True
    sortie.append(x)
    print(marque)
    print(sortie)
    file.append(x)
    print(file)
    while file !=[]:
        u = file.pop(0)
        print("-------------")
        print(u)
#         print("----------------------")
        for v in G[u]:
            if marque[v] == False:
                print(marque[v])
                print(marque)
                marque[v] = True
                sortie.append(v)
                print(sortie)
                file.append(v)
                print(file)
    return (sortie)

Graph=[[1],
       [0,3,4],
       [0],
       [1],
       [1,2]]
# print(BFS(Graph,3))
print("-------------------------------------------------")


#------------------------------------------------------------------------------
#entraînement 2



def liste_vers_matrice_adj(dico):
    """
    matrice - list, tableau 2D représentant une matrice d'adjacence associée à un graphe (orienté ou non)
    Sortie: dict - dictionnaire tel que:
                   les clefs sont les numéros associés aux sommets du graphe
                   les valeurs sont un tableau des voisins (ou successeurs) du sommet
    """
    matrice = [0]*len(dico)
    for i in range(len(matrice)):
        matrice[i] = [0]*len(matrice)
    for i in range (len(matrice)):
        valeur = dico[i]
        for k in range (len(valeur)):
            voisin = valeur[k]
            matrice[i][voisin] = 1
    return matrice

sommets =  ["C", "P", "S", "B", "CF", "L", "A", "T", "M"]
graph = {"C":["P","B","CF"],"P":["B","CF","S"],"S":["P","L"], "B":["C","P","CF","T","A"], "CF" : ["C","P","B","L","T"],
          "L":["S","P","CF","T","M"], "A":["B","T"], "T":["A","B","CF","L","M"], "M":["T","L"]}
print(liste_vers_matrice_adj(graph))
