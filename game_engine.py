"""
Projet Gomoku
Initialise une partie
Fait jouer le joueur et l'IA chacun leurs tour
"""
import random
import fonctions as ft
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def initialisation(N, depth):
    """
    Initialise le nombre de points a aligner, la grille et
    les lettres utilisées pour la légende.

    Puis lance le game_engine
    """
    Nb = 5
    alpha_utile = [ALPHABET[i] for i in range(N)]
    tab = ft.creer_tableau(N)
    game_engine(tab, N, Nb, alpha_utile, depth)

def game_engine(tab, N, Nb, alpha_utile, depth):
    """
    Commence par définir qui joue en premier et fait jouer l'IA si elle commence
    Ensuite, initialise la boucle d'actions servant a faire jouer le joueur
    Dans cette boucle, une multitude d'actions sont possibles
    """
    print("\nDébut d'une nouvelle partie, vous devez aligner {} pions".format(Nb))
    #définir qui commence
    starting = random.randint(0, 1)
    start = {0:"Vous commencez", 1:"L'IA commence"}
    print(start.get(starting))
    if starting == 1:
        jouer_ia(tab, N, Nb, alpha_utile, depth)
    #
    game_on = True
    while game_on:
        ft.afficher_tableau(tab, N, alpha_utile)
        action = input("Dans quelle case voulez vous jouer ?\n>>> ")
        if action == 'help':
            ft.help_()
        elif action == 'quit':
            game_on = False
        elif action == 'print':
            ft.afficher_tableau(tab, N, alpha_utile)
        elif 2 <= len(action) <= 3:
            lettre = action[0].upper()
            chiffre = action[1:]
            try:
                if ft.jouer(tab, N, int(chiffre), lettre, 1, alpha_utile) == -1:
                    print("Vous ne pouvez pas jouer dans cette case")
                else:
                    eval_joueur = ft.eval_position(tab, N, 1)
                    if eval_joueur >= 1000:
                        game_on = False
                        ft.afficher_tableau(tab, N, alpha_utile)
                        win(1)
                        break
                    elif eval_joueur == -1:
                        print("Plateau complet, égalité.")
                        game_on = False
                        break
                    print("Vous avez joué en {0}{1}".format(lettre, chiffre))
                    jouer_ia(tab, N, Nb, alpha_utile, depth)
                    eval_ia = ft.eval_position(tab, N, -1)
                    if eval_ia >= 1000:
                        game_on = False
                        ft.afficher_tableau(tab, N, alpha_utile)
                        win(-1)
                        break
                    elif eval_ia == -1:
                        print("Plateau complet, égalité.")
                        game_on = False
                        break
            except:
                print("Cette action n'existe pas")
                print("Entrez 'help' pour voir la liste des actions possibles")
        #actions de debugage
        # 'test' sert a afficher l'eval_position du joueur et de l'ia
        elif action == 'test':
            print("IA : {}".format(ft.eval_position(tab, N, -1)))
            print("joueur : {}".format(ft.eval_position(tab, N, 1)))
        # 'pr[case]' sert a afficher la score statique de cette case
        # exemple : prA1 pour avoir le score de la case A1
        elif action[:2].lower() == 'pr':
            sobel = ft.sobel(tab, N)
            try:
                ligne = int(action[3:])-1
                colonne = alpha_utile.index(action[2].upper())
                print(sobel[ligne][colonne])
            except:
                print()
        else:
            print("Cette action n'existe pas")
            print("Entrez 'help' pour voir la liste des actions possibles")

def jouer_ia(tab, N, Nb, alpha_utile, depth):
    """
    Fait jouer l'IA
    """
    eval_ia = ft.eval_position(tab, N, -1)
    eval_joueur = ft.eval_position(tab, N, 1)
    if eval_ia == 0 and eval_joueur == 0:
        #jouer au centre de la grille (tout premier coup)
        ligne = N//2
        colonne = alpha_utile[N//2-1]
    elif eval_joueur == 1000*(Nb-1)//Nb:
        #si le joueur est sur le point de gagner, jouer pour le bloquer
        #de la facon la plus directe possible
        coord = ft.eval_action(tab, N)[1]
        ligne = coord[1]+1
        colonne = alpha_utile[coord[0]]
    else:
        #jouer a l'endroit le plus interessant
        coord = ft.minimax(tab, N, -1, depth, True, -10000, +10000)[1]
        ligne = coord[1]+1
        colonne = alpha_utile[coord[0]]
    if ft.jouer(tab, N, ligne, colonne, -1, alpha_utile) == -1:
        print("l'IA n'a pas joué")
    else:
        print("l'IA a joué en {0}{1}".format(colonne, ligne))

def win(joueur):
    """
    Renvois un message en fonction du gagnant
    """
    if joueur > 0:
        print("\nVous avez gagné !")
    else:
        print("\nVous avez perdu...")
