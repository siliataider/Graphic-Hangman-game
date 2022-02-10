# -*- coding: utf-8 -*-
"""
#créé par: silia et etienne
#à 8:32
#pendu version console


@author: silia
"""

import random

file = open("mot.txt", "r")
mot=[]

for ligne in file:
    mot.append(ligne)

def choisirMot():
    a = random.random()* (len(mot)-1)
    a = int(a)
    print("on choisit le mot num: ", a)
    lettres_mot=[]
    for i in mot[a]:
        lettres_mot.append(i)
    del lettres_mot[-1]
    return(lettres_mot)

def affichage(mot_choisi, lettre_trouvee):
    underscore=[]
    for i in range (len(mot_choisi)):
        underscore.append("_")
    for i in lettre_trouvee:
        underscore[i]= mot_choisi[i]
    return(underscore)

def jeu(mot_a_deviner):
    lettre_trouvee=[0]
    essaie = 0
    perdu = 0
    lettre_utilisee=[]
    print("".join(affichage(mot_a_deviner,lettre_trouvee)))
    return(affichage(mot_a_deviner,lettre_trouvee))
    continu = True
    while continu == True:
        while len(lettre_trouvee) < len(mot_a_deviner):
            tentative=input("Entrer une lettre \n")
            if tentative in lettre_utilisee:
                print("Lettre déjà utilisée, vous venez de perdre une chance :(\n")
                del lettre_trouvee[-1]
            lettre_utilisee.append(tentative)
            lettre_bonne = False
            for i in range(len(mot_a_deviner)):
                if tentative == mot_a_deviner[i]:
                    lettre_trouvee.append(i)
                    print("lettre bonne\n")
                    lettre_bonne = True
            if lettre_bonne == False:
                print("Lettre fausse, reessayer!\n")
                essaie = essaie + 1
            if essaie == 5:
                print("Perdu! :(")
                perdu = 1
                break
            print("".join(affichage(mot_a_deviner,lettre_trouvee)))
            return(affichage(mot_a_deviner,lettre_trouvee))
            return(essaie)
        if perdu == 0:
            print("Bien joué! :)")
        continu = False
    file.close()

def mot_jeu(mot_a_deviner,lettre_trouvee):
    return(affichage(mot_a_deviner,lettre_trouvee))

#def lettre_trouvee(mot_a_deviner):
 #   for i in range(len(mot_a_deviner)):
  #          if tentative == mot_a_deviner[i]:
   #             lettre_trouvee.append(i)
    #            print("lettre bonne\n")
     #           lettre_bonne = True