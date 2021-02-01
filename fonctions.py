
"""
Projet Gomoku
toutes les fonctions utile au jeu
"""
import sys
from random import choice

def creer_tableau(N):
    """
    Crée un tableau de NxN cases toutes initalisées a 0
    et le retourne
    """
    tab = [[0 for i in range(N)] for j in range(N)]
    return tab

def afficher_tableau(tab, N, alpha_utile):
    """
    Affiche le tableau passé en parametre
    Les colones sont nommées par des lettres et les lignes par des chiffres
    Une case vide est affichée avec  ' '
    une case où le joueur a joué par 'X'
    et une case ou l'IA a joué par   'O'
    """
    d = {0:' ', 1:'X', -1:'O'}
    #affichage des lettres des colonnes
    if N >= 10:
        sys.stdout.write("\n    ||")
    else:
        sys.stdout.write("\n   ||")
    for lettre in alpha_utile:
        sys.stdout.write(' '+lettre+' |')
    #affichage de la délimitation
    if N >= 10:
        sys.stdout.write("\n----||")
    else:
        sys.stdout.write("\n---||")
    for i in range(len(alpha_utile)-1):
        sys.stdout.write('----')
    print('---|')
    #affichage des lignes
    for i, ligne in enumerate(tab):
        #affichage du numéro de la ligne
        if N >= 10 and i < 9:
            sys.stdout.write('  {} || '.format(i+1))
        else:
            sys.stdout.write(' {} || '.format(i+1))
        for case in ligne:
            sys.stdout.write("{} | ".format(d.get(case)))
        #affichage de la délimitation entre chaque ligne
        if N >= 10:
            sys.stdout.write("\n----||")
        else:
            sys.stdout.write("\n---||")
        for j in ligne:
            sys.stdout.write('---|')
        print()

def jouer(tab, N, ligne, colonne, joueur, alpha_utile):
    """
    Dans le tableau Tab, modifie la valeur de la case correspondant a la
    'ligne'-eme ligne et a la 'colonne'-eme colonne si et seulement si celle-ci
    est encore vide (c'est à dire, egale a 0)

    La valeur stockée est la valeur 'joueur' servant a differencier les joueurs
    (1 pour le joueur, -1 pour l'IA)

    retourne 0 si l'action a été jouée
    retourne -1 sinon
    """
    if colonne in alpha_utile and 0 < ligne < N+1:
        col = alpha_utile.index(colonne)
        if tab[ligne-1][col] == 0:
            tab[ligne-1][col] = joueur
            return 0
    return -1

def help_():
    """
    Affiche les commandes possibles
    """
    print(" help : pour connaitre toutes les commandes\n")
    print(" quit : pour quitter la partie en cours\n")
    print(" print : pour afficher la grille de Gomoku\n")
    print(" tout couple de la forme 'lettre''chiffre' : pour jouer dans une case libre")
    print("  (exemple : A1, pour jouer dans la premiere case de la premiere ligne)\n\n")
    print("Pour les débugueurs, des actions aditionnelles sont disponibles :")
    print(" test : pour afficher les eval_positions du joueur et de l'IA\n")
    print(" pr[case] : sert à afficher la score statique de cette case")
    print("  (exemple : prA1, pour avoir le score de la case A1)\n")

Gl = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [2, 3, 4, 5, 0, 5, 4, 3, 2],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0]]

Gc = [[0, 0, 0, 0, 2, 0, 0, 0, 0],
      [0, 0, 0, 0, 3, 0, 0, 0, 0],
      [0, 0, 0, 0, 4, 0, 0, 0, 0],
      [0, 0, 0, 0, 5, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 5, 0, 0, 0, 0],
      [0, 0, 0, 0, 4, 0, 0, 0, 0],
      [0, 0, 0, 0, 3, 0, 0, 0, 0],
      [0, 0, 0, 0, 2, 0, 0, 0, 0]]

Gd1 = [[2, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 3, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 4, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 5, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 5, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 4, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 3, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 2]]

Gd2 = [[0, 0, 0, 0, 0, 0, 0, 0, 2],
       [0, 0, 0, 0, 0, 0, 0, 3, 0],
       [0, 0, 0, 0, 0, 0, 4, 0, 0],
       [0, 0, 0, 0, 0, 5, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 5, 0, 0, 0, 0, 0],
       [0, 0, 4, 0, 0, 0, 0, 0, 0],
       [0, 3, 0, 0, 0, 0, 0, 0, 0],
       [2, 0, 0, 0, 0, 0, 0, 0, 0]]

def eval_action(tab, N):
    """
    Basé sur le le filtre sobel du traitement d'image, cette fonction
    renvoie les coordonnées du point (non encore joué)  ayant la plus
    grande valeur. Cela correspond au meilleur point où il faut jouer
    (que ce soit pour bloquer l'ennemi ou pour tenter de gagner)
    """
    coords = []
    val = -1
    coord = (0, 0)
    for x in range(N):
        for y in range(N):
            if tab[y][x] == 0:
                vl, vc, vd1, vd2 = 0, 0, 0, 0
                for xp in range(x-4, x+5):
                    for yp in range(y-4, y+5):
                        if 0 <= xp < N and 0 <= yp < N:
                            vl += tab[yp][xp]*Gl[yp-y+4][xp-x+4]
                            vc += tab[yp][xp]*Gc[yp-y+4][xp-x+4]
                            vd1 += tab[yp][xp]*Gd1[yp-y+4][xp-x+4]
                            vd2 += tab[yp][xp]*Gd2[yp-y+4][xp-x+4]
                if val < max(abs(vl), abs(vc), abs(vd1), abs(vd2)):
                    val = max(abs(vl), abs(vc), abs(vd1), abs(vd2))
                    coords = [(x, y)]
                elif val == max(abs(vl), abs(vc), abs(vd1), abs(vd2)):
                    coords.append((x, y))
    coord = choice(coords)
    return val, coord


def maximum(value1, value2):
    """
    value1 et value2 de sont la forme (valeur, coord)
    retourne le couple (valeur, coord) dont la valeur est la plus grande
    """
    val1 = value1[0]
    val2 = value2[0]
    if val1 >= val2:
        return value1
    return value2

def minimum(value1, value2):
    """
    value1 et value2 de sont la forme (valeur, coord)
    retourne le couple (valeur, coord) dont la valeur est la plus petite
    """
    val1 = value1[0]
    val2 = value2[0]
    if val1 <= val2:
        return value1
    return value2

def calcul_all_childs(tab, N, joueur):
    """
    Calcule tous les tableaux pouvant resulter du tableau actuel.
    Les stocke dans la liste Tab_childs et la retourne

    'joueur' est le joueur devant jouer dans cette simulation
    """
    tab_childs = []
    for x in range(N):
        for y in range(N):
            #créer une copie de la grille actuelle
            tab_copy = [list(ligne) for ligne in tab]
            #si la case est vide, créer une grille enfant (en jouant)
            #et sauvegarder cet enfant dans Tab_childs
            if tab_copy[y][x] == 0:
                tab_copy[y][x] = joueur
                tab_childs.append(tab_copy)
    return tab_childs

def minimax(tab, N, joueur, depth, maximizing_player, alpha, beta):
    """
    renvoie le coup minimisant la perte du joueur en prevoyant 'depth'
    tours dans le futur
    """
    if depth == 0:
        return eval_action(tab, N)
    #calculer toutes les grilles enfant de la grille actuelle
    #si depth est pair, c'est a 'joueur' de jouer
    #sinon, c'est a l'opposant
    if depth%2 == 0:
        tab_childs = calcul_all_childs(tab, N, joueur)
    else:
        tab_childs = calcul_all_childs(tab, N, -joueur)

    if maximizing_player:
        value = (-10000, (0, 0))
        for child in tab_childs:
            value = maximum(value, minimax(child, N, joueur, depth-1, False, alpha, beta))
            if value[0] >= beta:
                return value
            alpha = max(alpha, value[0])
    else:
        value = (+10000, (0, 0))
        for child in tab_childs:
            value = minimum(value, minimax(child, N, joueur, depth-1, True, alpha, beta))
            if alpha >= value[0]:
                return value
            beta = min(beta, value[0])
    return value

def sobel(tab, N):
    """
    Filtre sobel utilisé en traitment d'image.
    Pour chaque point du tableau, fait la somme des tout les voisins dans
    un rayon de 5 cases pondéré par les matrices Gl, Gc, Gd1 et Gd2.

    Elle n'est utilisée que pour le débugage
    """
    sobel = [[0 for i in range(N)] for j in range(N)]
    for x in range(N):
        for y in range(N):
            vl, vc, vd1, vd2 = 0, 0, 0, 0
            for xp in range(x-4, x+5):
                for yp in range(y-4, y+5):
                    if 0 <= xp < N and 0 <= yp < N:
                        vl += tab[yp][xp]*Gl[yp-y+4][xp-x+4]
                        vc += tab[yp][xp]*Gc[yp-y+4][xp-x+4]
                        vd1 += tab[yp][xp]*Gd1[yp-y+4][xp-x+4]
                        vd2 += tab[yp][xp]*Gd2[yp-y+4][xp-x+4]
            sobel[y][x] = max(abs(vl), abs(vc), abs(vd1), abs(vd2))
    return sobel

Gxl = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [1, 1, 1, 1, 1, 1, 1, 1, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]]

Gxc = [[0, 0, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 0]]

Gxd1 = [[1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1]]

Gxd2 = [[0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0]]

def eval_position(tab, N, joueur):
    """
    Fonctionne sur le meme principe que la fonction eval_action, mais les cases
    ne sont pas coéficientées. Cela reviens a compter le nombre de point selon
    la dimension que l'on regarde. On obtiens donc le point avec le plus de
    pions autour de lui selon une dimension.

    Apres, cela, la fonction vérifie le nombre de point connexe et renvois
    un score sur 1000
    """
    if joueur == 1:
        val = -1
    else:
        val = 1
    coord = (0, 0)
    direc = ''
    compteur_zero = 0
    for x in range(N):
        for y in range(N):
            if tab[y][x] == 0:
                compteur_zero += 1
            vl, vc, vd1, vd2 = 0, 0, 0, 0
            for xp in range(x-4, x+5):
                for yp in range(y-4, y+5):
                    if 0 <= xp < N and 0 <= yp < N:
                        vl += tab[yp][xp]*Gxl[yp-y+4][xp-x+4]
                        vc += tab[yp][xp]*Gxc[yp-y+4][xp-x+4]
                        vd1 += tab[yp][xp]*Gxd1[yp-y+4][xp-x+4]
                        vd2 += tab[yp][xp]*Gxd2[yp-y+4][xp-x+4]
            #recherche de la direction avec la plus grande valeur
            d = {-1:min(val, vl, vc, vd1, vd2), 1:max(val, vl, vc, vd1, vd2)}
            if d.get(joueur) == vl:
                val = vl
                coord = (x, y)
                direc = 'ligne'
            elif d.get(joueur) == vc:
                val = vc
                coord = (x, y)
                direc = 'col'
            elif d.get(joueur) == vd1:
                val = vd1
                coord = (x, y)
                direc = 'diag1'
            elif d.get(joueur) == vd2:
                val = vd2
                coord = (x, y)
                direc = 'diag2'
    #vérification si il y a encore des cases libres
    if compteur_zero == 0:
        return -1
    #recherche du nb de pions
    max_points_alignes = 0
    compteur = 0
    if direc == 'ligne':
        ligne = coord[1]
        for colonne in range(coord[0]-4, coord[0]+5):
            if 0 <= colonne < N:
                if tab[ligne][colonne] == joueur:
                    compteur += 1
                else:
                    if compteur > max_points_alignes:
                        max_points_alignes = compteur
                    compteur = 0
        if compteur > max_points_alignes:
            max_points_alignes = compteur
    elif direc == 'col':
        colonne = coord[0]
        for ligne in range(coord[1]-4, coord[1]+5):
            if 0 <= ligne < N:
                if tab[ligne][colonne] == joueur:
                    compteur += 1
                else:
                    if compteur > max_points_alignes:
                        max_points_alignes = compteur
                    compteur = 0
        if compteur > max_points_alignes:
            max_points_alignes = compteur
    elif direc == 'diag1':
        ligne = coord[1]-4
        colonne = coord[0]-4
        for i in range(9):
            if 0 <= colonne+i < N and 0 <= ligne+i < N:
                if tab[ligne+i][colonne+i] == joueur:
                    compteur += 1
                else:
                    if compteur > max_points_alignes:
                        max_points_alignes = compteur
                    compteur = 0
        if compteur > max_points_alignes:
            max_points_alignes = compteur
    else:
        ligne = coord[1] - 4
        colonne = coord[0] + 4
        for i in range(9):
            if 0 <= colonne-i < N and 0 <= ligne+i < N:
                if tab[ligne+i][colonne-i] == joueur:
                    compteur += 1
                else:
                    if compteur > max_points_alignes:
                        max_points_alignes = compteur
                    compteur = 0
        if compteur > max_points_alignes:
            max_points_alignes = compteur
    return 1000*max_points_alignes//5
