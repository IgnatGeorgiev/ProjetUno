from random import randint
sens = 0
def MelangePaquet() :
    """Retourne le paquet mélangé"""
    Paquet = []
    for i in range(0,108) : # remplissage le paquet
        val = randint(1,108)
        if val in Paquet :
            val = randint(1,108) # filtrage : Pas 2 fois la même valeur
        Paquet.append(val)
    return Paquet
Cartes = {1:0, 2:1,3:1, 4:2, 5:2, 6:3, 7:3, 8:4, 9:4, 10:5, 11:5, 12:6, 13:6, 14:7, 15:7, 16:8, 17:8, 18:9, 19:9, 20 :10, 21:10, 22:11, 23 :11, 24:12, 25:12 } # Dictionnaire indice(valeur) : numéro
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
        if indiceVnumero(e)==10 and indiceVcouleur(e) == couleur : Indic = "Oui"   #Le joueur possède un +2 de meme couleur que la carte courante
        if indiceVcarte(e) == "+4" : Indic = "Oui"    #Le joueur possède une carte de meme numero que la carte courante ou un +4
        if numero != 10 :
            if indiceVnumero(e) == numero : Indic = "Oui"
        if numero != 10 and numero != 14 :
            if indiceVnumero(e) == 13 : Indic = "Oui"   #Le joueur peut jouer un joker sauf sur un +  
            elif  indiceVcouleur(e)==couleur : Indic = "Oui"    #peut jouer une carte de meme couleur que la carte courante
            elif numero == 13 : Indic = "Oui"       #peut jouer un joker
        else : Indic = Indic   # Impossibilité de jouer
    return Indic
def nbreapiocher(lcard,main) :
    """Renvoie le nombre de carte à piocher"""
    compteur2 = 0 # compte le nombre de carte à piocher selon les +2
    compteur4 = 0 # compte le nombre de carte à piocher selon les +4
    if indiceVnumero(lcard) == 10 : compteur2+=2      #la carte courante est un +2
    elif indiceVnumero(lcard) == 14 : compteur4+=4     #la carte courante est un +4
    if verifieur(jeu,main) == 'Oui':      
        aux = 0     # possibilité de jouer,0 carte à piocher
    else :
        aux = compteur2+compteur4
        if aux == 0 : aux+=1     #impossibilité de jouer et aucune carte +,doit piocher 1 carte
    return aux
def choixcarte(main,jeu) :
    """Renvoie la carte choisie et jouable"""
    if verifieur(jeu,main) == 'Oui' :  #possibilité de jouer
        MSG = "Quelle carte voulez vous jouez ? (1ere,2eme,...) : "
        choix = int(input(MSG))   #position de la carte choisie par l'utilisateur
        lst = [main[choix-1]]    #Rangement de cette carte dans une liste
        while verifieur(jeu,lst) == 'Non' :  #Filtrage: on veut que la carte choisie soit jouable
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
        piocher_V2(paquet,main,nombrecartes)  #Création de la main de chaque joueur
        joueurs[nom] = main #Rangement de la main du joueur dans le dictionnaire
    return joueurs
def sensderotation(dernierecarte,joueurs,joueurprec):
    """Sens de rotation et prochain joueur"""
    global sens  
    listejoueurs = list(joueurs.keys())
    imax = len(listejoueurs)-1
    prochainjoueur=""
    for joueur in listejoueurs:
        if joueur == joueurprec: # Recherche du joueur donné en argument dans la liste
                if indiceVnumero(dernierecarte) == 11 and sens == 0:    #Change sens
                    sens = 1
                    if listejoueurs.index(joueur) == 0: 
                        prochainjoueur = listejoueurs[imax]
                    else:
                        prochainjoueur = listejoueurs[listejoueurs.index(joueur)-1]
                elif indiceVnumero(dernierecarte) == 11 and sens == 1:
                    sens = 0
                    if listejoueurs.index(joueur) == 0:
                        prochainjoueur = listejoueurs[imax]
                    else:
                        prochainjoueur = listejoueurs[listejoueurs.index(joueur)-1]
                        
                elif indiceVnumero(dernierecarte) == 12:   #passe tour
                    if listejoueurs.index(joueur) == imax:
                        prochainjoueur = listejoueurs[1]
                    elif listejoueurs.index(joueur) == imax-1:
                        prochainjoueur = listejoueurs[0]
                    else :
                        prochainjoueur = listejoueurs[listejoueurs.index(joueur)+2]
                else:  #rotation normale
                    if listejoueurs.index(joueur) == imax:
                         prochainjoueur = listejoueurs[0]
                    else:
                        prochainjoueur = listejoueurs[listejoueurs.index(joueur)+1]
    return prochainjoueur
def testvictoire(joueurs,joueurcourant):
    """Test de victoire et fin de partie"""
    return joueurs[joueurcourant] == [] #Renvoie True si la main du joueur est vide
def tourdejeu(joueur,joueurs,jeu,pioche):
    """Tour De Jeu"""
    if jeu != [] : #La partie a commencé 
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
                    if indiceVnumero(e) == 10 and len(jeu)!=1 or indiceVcarte(e) == "+4" and len(jeu)!=1: jeu.remove(e) 
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
aux = 0 ; i = 0; j=0  #variables utilisée dans la fonction tour de jeu 
sens = 0 # variable utilisée dans la fonctioon sensderotation
while not testvictoire(dic,player) :  # Vérifie si le joueur courant a gagné
    lst = []; lst3 = []
    for e in dic[player] :
        lst.append(indiceVcarte(e))  #affiche la main du joueur avec le nom des cartes
    if jeu != [] :
        for e in jeu :
            lst3.append(indiceVcarte(e))
        print(lst3)  #affiche le jeu avec les noms des cartes
    print(player , lst)
    player = tourdejeu(player,dic,jeu,paquet)
print("Le gagnant est", player)
del dic[player] #supprime la main du joueur gagnant puis affiche les mains des perdants
for e in dic :
    lst2 = []
    for x in dic[e]:
        lst2.append(indiceVcarte(x))
    dic[e] = lst2
print(dic)

       
