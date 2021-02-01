"""
Projet Gomoku
Main : lance une partie
"""
import game_engine as GE
print("Voulez vous jouer contre :")
print("1) Une IA simple sur un plateau de 19x19")
print("2) Une IA plus intelligente sur un plateau de 11x11")
#selection de la difficulté
NOTOK = True
while NOTOK:
    DIF = input(">>> ")
    if int(DIF) not in [1, 2]:
        print("Veuillez entrer une valeur correcte")
    else:
        NOTOK = False
#définition de la difficulté
if int(DIF) == 1:
    N = 19
    DEPTH = 0
else:
    N = 11
    DEPTH = 2
#lancement du jeu
GE.initialisation(N, DEPTH)
