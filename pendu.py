"""
Spyder Editor

#créé par: silia et etienne
#à 8:32
#pendu version console
"""

from fonctions import *

jouer = '1'
while jouer == '1':
    mot_a_deviner=choisirMot()
    jeu(mot_a_deviner)
    jouer = input("Appuyer sur 1 pour rejouer\n")
print("Merci d'avoir joué!")
# -*- coding: utf-8 -*-


