# header
"""
qui : Etienne FAucher   
quand : le 08/12/2020 
Interface graphique du pendu
TODO : rien
"""
from fonctions import *

#On choisit un mot
mot_a_deviner=choisirMot()
#On affiche le mot à l'utilisateur (avec underscores)
afficheage_uti=mot_jeu(mot_a_deviner,[0])
print(afficheage_uti)



#a,b,c=jeu(mot_a_deviner)
#importation des bibiothèques nécessaires
from tkinter import Tk, Label, Button, Frame, Entry, PhotoImage, Canvas, Menu

# création de la fenêtre graphique
mw = Tk()
mw.title('Jeu du pendu')
#Taille de fenêtre
mw.geometry('480x360+900+150')
mw.configure(bg='white')

menubar= Menu(mw)
menufichier= Menu(menubar,tearoff=0)
menufichier.add_command(label="Quitter", command = mw.destroy)
menubar.add_cascade(label="Fichier", menu=menufichier)
mw.config(menu=menubar)
#partition de la fenêtre et affichage
jeu= Frame(mw, relief='flat', bg='white')
jeu.pack(side='left')

dessin= Frame(mw, relief='sunken', bg='white')
dessin.pack(side='right')

#On gere les partitions
Label(jeu, textvariable= afficheage_uti, fg='blue').pack(side="top")
Label(dessin, text="Votre pendu s'affiche ici", fg='blue').pack(side='top')

Entry(jeu, text="Rentrez votre lettre ici").pack()
#création du widget "Bonjour le monde"
labelHello = Label(mw, text = "Bienvenue sur le jeu du pendu", fg = 'blue')
# positionnement du widget
labelHello.pack()
# cration du widget bouton
buttonPropos= Button (jeu, text= "Proposer", fg='gray', command="")
buttonQuitt = Button (jeu, text = "QUITTER", fg = 'red', command = mw.destroy)

canevas= Canvas(dessin, width='950', height='950')
filename = PhotoImage(file = "bonhomme1.gif")
image = canevas.create_image(150, 150, image=filename)
canevas.pack()
# positionnement du widget
buttonPropos.pack()
buttonQuitt.pack()


#lancement du gestionnaire d'événements
mw.mainloop()
