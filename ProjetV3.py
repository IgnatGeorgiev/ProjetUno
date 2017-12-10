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
Multi = { 26:13, 27:13, 28:13, 29:13, 30:13, 31:13, 32:13, 33:13 } ### les +4 sont les 4 dernieres cartes
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
    elif n in range(76,101) : num = Cartes[n-75]
    elif n in range(101,105) : num = 13
    else : num = 14
    return num

def indiceVcarte(n) :
    """retourne valeur et couleur"""
    if indiceVnumero(n) == 10 :
        aux = "+2"+" "+indiceVcouleur(n)
    elif indiceVnumero(n) == 11:
        aux = "Change sens"+" "+indiceVcouleur(n)
    elif indiceVnumero(n) == 12 :
        aux = "passe tour"+" "+indiceVcouleur(n)
    elif indiceVnumero(n) == 13 :
        aux = "Joker"
    elif indiceVnumero(n) == 14 :
        aux = '+4'
    else : aux = str(indiceVnumero(n))+" "+indiceVcouleur(n)
    return aux
#### pioche
def piocher(paquet) :
    """Pioche la dernière carte du paquet"""
    carte  = paquet.pop()
    return carte
#### main du joueur
def piocher_V2(pioche,main,nb) :
    """ Modifie la main du joueur et la pioche"""
    for e in range(0,nb) :
        main.append(pioche.pop())
#### Affichage de la main
def affich_main(main) :
    """affiche la main du joueur avec couleur et valeur""" 
    for e in main :
        print(indiceVcarte(e))
#### Pioche vide ?piocher_V2
def piochmaker(pioche,pile) :
    """ Modifie la pioche pour en créer une nouvelle
    à partir de la pile de jeu"""
    lastcard = pile.pop()
    for e in pile:
        pioche.append(e)
        pile.remove(e) # I remove all the elements of the pile to reset it
    pile = [lastcard] # I put back the last card in the pile to allow players to know what they have to play next
    random.shuffle(pioche) # To mix pile cards with pioche cards
#### PARTIE B
def verifieur(jeu,main) :  #Jeu est une liste 
    """Vérifie si on peut poser une carte"""
    Indic = "Non"
    couleur = indiceVcouleur(jeu[len(jeu)-1])
    numero = indiceVnumero(jeu[len(jeu)-1])
    for e in main :
        if indiceVcouleur(e) == couleur or indiceVnumero(e) == numero or indiceVcarte(e) == "+4" : Indic = "Oui"
        if numero != 10 and numero != 14 :
            if indiceVnumero(e) == 13 : Indic = "Oui"
        elif numero == 13 : Indic = "Oui"
        else : Indic = Indic
    return Indic
def nbreapiocher(jeu,main) :
    """Renvoie le nombre de carte à piocher"""
    compteur2 = 0
    compteur4 = 0
    for e in jeu :
        if indiceVnumero(e) == 10 : compteur2+=1
        elif indiceVnumero(e) == 14 : compteur4+=1
    if verifieur(jeu,main) == 'Oui':
        aux = 0
    else :
        aux = compteur2*2+compteur4*4
        if aux == 0 : aux+=1
    return aux

def choixcarte(main,jeu) :
    """Renvoie la carte choisie et jouable"""
    if verifieur(jeu,main) == 'Oui' :
        MSG = "Quelle carte voulez vous jouez ? (1ere,2eme,...) : "
        choix = int(input(MSG))
        lst = [main[choix-1]]
        while verifieur(jeu,lst) == 'Non' :
             choix = int(input(MSG))
             lst = [main[choix-1]]
        return lst[0]
#### Partie C
def gestiondesjoueurs(paquet):
    """Gestion des joueurs"""
    nombrejoueurs = int(input("Nombre des joueurs? "))
    joueurs = {}
    nombrecartes = int(input("Nombres de cartes pour chacun? "))
    paquet = MelangePaquet()
    for i in range(0,nombrejoueurs):
        main = []
        nom = input("Nom de joueur? ")
        piocher_V2(paquet,main,nombrecartes)
        joueurs[nom] = main
    return joueurs
def sensderotation(dernierecarte,joueurs,joueurprec):
    """Sens de rotation et prochain joueur"""
    listejoueurs = list(joueurs.keys())
    imax = len(listejoueurs)-1
    prochainjoueur=""
    for joueur in listejoueurs:
        if joueur == joueurprec:
            if indiceVnumero(dernierecarte) == 11:
                if listejoueurs.index(joueur) == 0:
                    prochainjoueur = listejoueurs[imax]
                else:
                    prochainjoueur = listejoueurs[listejoueurs.index(joueur)-1]

            elif indiceVnumero(dernierecarte) == 12:
                if listejoueurs.index(joueur) == imax:
                    prochainjoueur = listejoueurs[1]
                elif listejoueurs.index(joueur) == imax-1:
                    prochainjoueur = listejoueurs[0]
                else :
                    prochainjoueur = listejoueurs[listejoueurs.index(joueur)+2]
            else:
                if listejoueurs.index(joueur) == imax:
                     prochainjoueur = listejoueurs[0]
                else:
                    prochainjoueur = listejoueurs[listejoueurs.index(joueur)+1]
    return prochainjoueur
def testvictoire(joueurs,joueurcourant):
    """Test de victoire et fin de partie"""
    return joueurs[joueurcourant] == []

def tourdejeu(joueur,joueurs,jeu,pioche):
    """Tour De Jeu"""
    i=0
    cartejoue =""
    #while i < 3: ### Why
    if jeu != [] :
        carteapioch = nbreapiocher(jeu,joueurs[joueur])
        if carteapioch > 0 :
            if pioche == [] : piochmaker(pioche,jeu)
            piocher_V2(pioche,joueurs[joueur],carteapioch)
            i+=1
        else:
            cartejoue = choixcarte(joueurs[joueur],jeu)
            joueurs[joueur].remove(cartejoue)
            jeu.append(cartejoue)
            #break
    else :
        choix = int(input("Quelle carte voulez vous jouez ?(1ere,2eme,...) "))
        cartejoue = joueurs[joueur][choix-1]
        joueurs[joueur].remove(cartejoue)
        jeu.append(cartejoue)
    prochainjoueur= sensderotation(jeu[len(jeu)-1],joueurs,joueur)
    return prochainjoueur
#### MAIN PROGRAM
paquet = MelangePaquet()
dic = gestiondesjoueurs(MelangePaquet)
player = list(dic.keys())[0]
jeu = []
while not testvictoire(dic,player) :
    lst = []; lst3 = []
    for e in dic[player] :
        lst.append(indiceVcarte(e))
    if jeu != [] :
        for e in jeu :
            lst3.append(indiceVcarte(e))
        print(lst3)
    print(player , lst)
    player = tourdejeu(player,dic,jeu,paquet)
print("Le gagnant est", player)
del dic[player]
for e in dic :
    for x in dic[e]:
        lst2 = []
        lst2.append(indiceVcarte(x))
    dic[e] = lst2
print(dic)

       
    

