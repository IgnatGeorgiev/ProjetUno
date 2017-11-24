from random import randint
def MelangePaquet() :
    """Retourne le paquet mélangé"""
    Paquet = []
    for i in range(0,108) :
        val = randint(1,108)
        if val in Paquet :
            val = randint(1,108)
        Paquet.append(val)
    return Paquet

####Conversions
Cartes = {1:0, 2:1,3:1, 4:2, 5:2, 6:3, 7:3, 8:4, 9:4, 10:5, 11:5, 12:6, 13:6, 14:7, 15:7, 16:8, 17:8, 18:9, 19:9, 20 :10, 21:10, 22:11, 23 :11, 24:12, 25:12 }
def indiceVcouleur(n):
    """Renvoie la couleur de la carte correspondant a l'indice
        Précondition : 1<=n<=108"""
    if n in range(1,26) : couleur='rouge'
    elif n in range(26,51) : couleur = 'bleu'
    elif n in range(51,76) : couleur = 'jaune'
    elif n in range(76,101) : couleur = 'vert'
    else : couleur ='multicolore'
    return couleur
def indiceVnumero(n):
    """Renvoie le numéro correspondant à la carte
        Précondition : 1<=n<=100"""
    if n in range(1,26) : num = Cartes[n]
    elif n in range(26,51) : num = Cartes[n-25]
    elif n in range(51,76) : num = Cartes[n-50]
    else : couleur = num = Cartes[n-75]
    return num

def indiceVcarte(n) :
    """retourne valeur et couleur"""
    return str(indiceVnumero(n))+" "+indiceVcouleur(n)
#### pioche
def piocher(paquet) :
    """Pioche la dernière carte du paquet"""
    carte  = paquet.pop()
    return carte
#### main du joueur
def piocher_V2(pioche,main,nb) :
    """ Modifie la main du joueur et la pioche"""
    for e in range(0,nb) :
        main.append(pioche(pioche))
#### Affichage de la main
def affich_main(main) :
    """affiche la main du joueur avec couleur et valeur""" 
    for e in main :
        print(indiceVcarte(e))
#### Pioche vide ?
def piochmaker(pioche,pile) :
    """ Modifie la pioche pour en créer une nouvelle
    à partir de la pile de jeu"""
    lastcard = pile.pop()
    for e in pile:
        pioche.append(e)
        pile.remove(e) # I remove all the elements of the pile to reset it
    pile = [lastcard] # I put back the last card in the pile to allow players to know what they have to play next
    random.shuffle(pioche) # To mix pile cards with pioche cards

    
