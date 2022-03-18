#entrainement 8
#solution du prof

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


#L1 = {0:[1,4,3], 1:[0,4], 2:[0,3,4], 3:[2,4], 4: [1,2,3,0]}
#print(liste_vers_matrice_adj(L1))


#____________________________________________________________________________________


#entrainement 9
#solution de mathieu

def dico_vers_matrice_pond(dico):
    """
    dico - dictionnaire tel que:
                les clefs sont les numéros associés aux sommets d'un graphe pondéré non orienté
                les valeurs sont un dictionnaire {voisins: pondération } du sommet
    Sortie: list - tableau 2D représentant une matrice de pondération associée au graphe
    """
    liste = [0]*len(dico)
    for i in range(len(liste)):
        liste[i] = [0]*len(liste)
    for cle, element in dico.items():
        for key, elem in element.items():
            liste[cle][key] = elem
    return liste

L3 = {0: {2: 3, 3: 1}, 1: {2: 4, 3: 2, 4: 1}, 2: {0: 3, 1: 4, 3: 6}, 3: {0: 1, 1: 2, 2: 6, 4: 5}, 4: {1: 1, 3: 5}}
print(dico_vers_matrice_pond(L3))

#____________________________________________________________________________________



#entrainement 10
#solution mathieu

def matrice_pond_vers_dico(matrice):
    """
    matrice - list, tableau 2D représentant une matrice de pondération associée à un graphe pondéré
    Sortie: dict - dictionnaire tel que:
                   les clefs sont les numéros associés aux sommets du graphe
                   les valeurs sont un dictionnaire {voisins: pondération} du sommet
    """
    dico = dict()
    for i in range(len(matrice)):
        dico[i] = 0
    dict_temp = dict()
    for cle, elem in dico.items():
        for j in range(len(matrice)):
            if matrice[cle][j] != 0:
                dict_temp.udate({j:matrice[cle][j]})
        dico[cle] = dict_temp
        dict_temp = {}
    return dico

#__________________________________________________________________________________________

#entrainement 11
#solution mathieu

def est_symetrique(matrice):
    """
    matrice - list, tableau 2D d'entiers représentant une matrice carrée
    Sortie: bool - True si la matrice est symétrique, False sinon
    """
    for i in range(len(matrice)):
      for j in range(len(matrice)):
        if matrice[i][j] != matrice[j][i]:
          return False
    return True
  
  
  #________________________________________________________________________________________
  
  
  #entrainement 12
  #solution prof
  
  def est_pondere(matrice):
    """
    matrice - list, tableau 2D d'entiers représentant une matrice carrée
    Sortie: bool - True si la matrice comporte des valeurs autre que 0 ou 1,
                   False sinon
    """
    for i in range(len(matrice)):
      for j in range(len(matrice)):
        if matrice[i][j] !=0 and matrice[i][j] !=1:
          return True
    return False
       
