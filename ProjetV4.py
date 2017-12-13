from random import randint
sens = 0
def MelangePaquet() :
    """Retourne le paquet mélangé"""
    Paquet = []
    for i in range(0,108) : # Boucle 108 fois pour remplir le paquet
        val = randint(1,108)
        if val in Paquet :
            val = randint(1,108) # Pas 2 fois la même valeur
        Paquet.append(val)
    return Paquet
Cartes = {1:0, 2:1,3:1, 4:2, 5:2, 6:3, 7:3, 8:4, 9:4, 10:5, 11:5, 12:6, 13:6, 14:7, 15:7, 16:8, 17:8, 18:9, 19:9, 20 :10, 21:10, 22:11, 23 :11, 24:12, 25:12 } # Dictionnaire indice(valeur) : numéro
Multi = { 26:13, 27:13, 28:13, 29:13, 30:14, 31:14, 32:14, 33:14} ### les +4 sont les 4 dernieres cartes
def indiceVcouleur(n): # n est l'indice
    """Renvoie la couleur de la carte correspondant a l'indice
        Précondition : 1<=n<=108"""
    if n in range(1,26) : couleur='rouge' # couleur est une variable auxiliaire
    elif n in range(26,51) : couleur = 'bleu'
    elif n in range(51,76) : couleur = 'jaune' # les cartes sont rangées dans l'ordre : rouge,bleu,jaune,vert,multicolores 
    elif n in range(76,101) : couleur = 'vert'
    else : couleur ='multicolore' # 100<=n<=108
    return couleur
def indiceVnumero(n): # n est l'indice
    """Renvoie le numéro correspondant à la carte
        Précondition : 1<=n<=100"""
    if n in range(1,26) : num = Cartes[n] # num est une variable auxiliaire
    elif n in range(26,51) : num = Cartes[n-25]
    elif n in range(51,76) : num = Cartes[n-50]
    elif n in range(76,101) : num = Cartes[n-75] # Utilisation du dictionnaire
    elif n in range(101,105) : num = 13
    else : num = 14 # 105<=n<=108 
    return num
def indiceVcarte(n) :  # n est l'indice de la carte
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
def piocher(paquet) :
    """Pioche la dernière carte du paquet"""
    carte  = paquet.pop()
    return carte
def piocher_V2(pioche,main,nb) :
    """ Modifie la main du joueur et la pioche"""
    for e in range(0,nb) : # pioche un nombre nb de fois donné en argument
        main.append(pioche.pop())
def affich_main(main) :
    """affiche la main du joueur avec couleur et valeur""" 
    for e in main :
        print(indiceVcarte(e))
def piochmaker(pioche,pile) :
    """ Modifie la pioche pour en créer une nouvelle
    à partir de la pile de jeu"""
    lastcard = pile.pop() # garde de côté la dernière carte de la pile
    for e in pile:
        pioche.append(e)
        pile.remove(e) 
    pile = [lastcard] # Remet la carte dans la pile de jeu pour la suite
    random.shuffle(pioche) 
#### PARTIE B
def verifieur(jeu,main) :  #Jeu est une liste 
    """Vérifie si on peut poser une carte"""
    Indic = "Non"
    couleur = indiceVcouleur(jeu[len(jeu)-1])
    numero = indiceVnumero(jeu[len(jeu)-1])
    for e in main :
        if indiceVcarte(e)=='+2' and indiceVcouleur(e) == couleur : Indic = "Oui"
        if indiceVnumero(e) == numero or indiceVcarte(e) == "+4" : Indic = "Oui"
        if numero != 10 and numero != 14 :
            if indiceVnumero(e) == 13 : Indic = "Oui"
            elif indiceVnumero(e) == 11 and indiceVcouleur(e)==couleur or indiceVnumero(e) == 12 and indiceVcouleur(e)==couleur : Indic = "Oui"
            elif  indiceVcouleur(e)==couleur : Indic = "Oui"
        if numero == 13 : Indic = "Oui"
        else : Indic = Indic
    return Indic
def nbreapiocher(lcard,main) :
    """Renvoie le nombre de carte à piocher"""
    compteur2 = 0 
    compteur4 = 0 
    if indiceVnumero(lcard) == 10 : compteur2+=2
    elif indiceVnumero(lcard) == 14 : compteur4+=4
    if verifieur(jeu,main) == 'Oui':
        aux = 0
    else :
        aux = compteur2+compteur4
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
    global sens
    listejoueurs = list(joueurs.keys())
    imax = len(listejoueurs)-1
    prochainjoueur=""
    for joueur in listejoueurs:
        if joueur == joueurprec:
                if indiceVnumero(dernierecarte) == 11 and sens = 0:
                    sens = 1
                    if listejoueurs.index(joueur) == 0:
                        prochainjoueur = listejoueurs[imax]
                    else:
                        prochainjoueur = listejoueurs[listejoueurs.index(joueur)-1]
                elif indiceVnumero(dernierecarte) == 11 and sens = 1:
                    sens = 0
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
    if jeu != [] :
        carteapioch = nbreapiocher(jeu[len(jeu)-1],joueurs[joueur])
        while carteapioch == 0 and  indiceVcarte(jeu[len(jeu)-1]) == "+2" or carteapioch == 0 and indiceVcarte(jeu[len(jeu)-1]) == "+4" :
            if indiceVcarte(jeu[len(jeu)-1]) == "+2" :global i; i += 2
            elif indiceVcarte(jeu[len(jeu)-1]) == "+4": global j ;j += 4
            global aux
            aux+= i+j
        if carteapioch > 0 :
            if aux > 0 : carteapioch = aux
            if pioche == [] : piochmaker(pioche,pile)
            piocher_V2(pioche,joueurs[joueur],carteapioch)
            if carteapioch>1 :
                for e in jeu :
                    if indiceVnumero(e) == 10 or indiceVcarte(e) == "+4" and len(jeu)!=1: jeu.remove(e) 
        else:
            cartejoue = choixcarte(joueurs[joueur],jeu)
            joueurs[joueur].remove(cartejoue)
            jeu.append(cartejoue)
    else :
        choix = int(input("Quelle carte voulez vous jouez ?(1ere,2eme,...) "))
        cartejoue = joueurs[joueur][choix-1]
        joueurs[joueur].remove(cartejoue)
        jeu.append(cartejoue)
    prochainjoueur = sensderotation(jeu[len(jeu)-1],joueurs,joueur)
    return prochainjoueur
#### MAIN PROGRAM
paquet = MelangePaquet()
dic = gestiondesjoueurs(MelangePaquet)
player = list(dic.keys())[0]
jeu = []
pile = []
aux = 0 ; i = 0; j=0
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
    lst2 = []
    for x in dic[e]:
        lst2.append(indiceVcarte(x))
    dic[e] = lst2
print(dic)

       
    

