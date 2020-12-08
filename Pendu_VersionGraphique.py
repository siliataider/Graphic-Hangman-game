# -*- coding: utf-8 -*- 
"""
qui : Etienne Faucher 
quand : le 08/12/2020 
Interface graphique du pendu
TODO : rien
"""
#Importation
from  tkinter import Tk, Label, Button, Frame, Entry, PhotoImage, Canvas, Menu, StringVar
import random
#Importation des mots
file = open("mot.txt", "r")
mot=[]
for ligne in file:
    mot.append(ligne)



#Definition (programme)

def ChoixMot(mot):
    Mot=random.choice(mot) #choix random d'un mot dans la liste
    return Mot

def Gagne(Mot,LettresTrouvees):
    i=0
    for l in Mot:
        if l in LettresTrouvees: #ajouter 1 au compteur si la lettre_trouvee du mot est dans la liste de lettres trouvees
            i+=1
    if i==len(Mot): #si le nombre de lettres trouvees est égal à la longueur du mot retourner True
        return True

def AffichageBonhomme():
    global nbchance
    if nbchance==6:
        item = Canevas.create_image(150,150,image=image2)
    if nbchance==5:
        item = Canevas.create_image(150,150,image=image3)
    if nbchance==4:
        item = Canevas.create_image(150,150,image=image4)
    if nbchance==3:
        item = Canevas.create_image(150,150,image=image5)
    if nbchance==2:
        item = Canevas.create_image(150,150,image=image6)
    if nbchance==1:
        item = Canevas.create_image(150,150,image=image7)
    if nbchance==0:
        item = Canevas.create_image(150,150,image=image8)      


def AffichageMot(Mot,LettresTrouvees):
    a = ""
    for i, L in enumerate(Mot): 
        if i==0 or L in LettresTrouvees: #afficher la première lettre_trouvee ainsi que les autres lettres trouvées
            a+=L
        else: #afficher _ pour les lettres non trouvees
            a+=" _"
    mot_affiche.set(a)
    return a

def AffichLettresFausses(LettresFausses):
    A=""
    for i in LettresFausses:
        A+=i
        A+=" "
    List.set("Lettres fausses : "+A)
    return A

def Rejouer():
    global Mot,LettresTrouvees,LettresFausses,nbchance
    Mot=ChoixMot(mot) #On choisit un mot
    LettresTrouvees=[Mot[0]]#réinitialistation des lettres trouvees
    LettresFausses=[]
    nbchance = 7 #On réinitialise les essais
    Pendu()
    return Mot,LettresTrouvees,LettresFausses,nbchance

 
def Verif():
    """
    Cette fonction vérifie que la lettre_trouvee donnée par l'utilisateur est bien dans le mot
    """
    global LettresTrouvees,LettresFausses,Mot,nbchance
    l=lettre_trouvee.get()
    lettre_trouvee.set('')
    
    if l in Mot: #si la lettre_trouvee est dans le mot
            LettresTrouvees.append(l)#on ajoute la lettre_trouvee à la liste de lettres trouvees
            AffichageMot(Mot,LettresTrouvees)#afficher le mot avec la nouvelle lettre_trouvee trouvee
        
    else :
        nbchance=nbchance-1 #enlever une chance à l'utilisateur
        LettresFausses.append(l) #ajout de la lettre_trouvee dans la liste de lettres fausses
        AffichageBonhomme()
        Coups_restants.set("Nombre de coups restants: "+str(nbchance))
        AffichLettresFausses(LettresFausses) #On actualise la liste de lettres fausses


def Pendu():
    global Mot,LettresTrouvees,LettresFausses,nbchance
    AffichageMot(Mot,LettresTrouvees) #Affichage du mot avec les lettres trouvées
    if nbchance>0:#tant que le joueur n'a pas épuisé ses chances
        Verif()
    
    




#Debut du jeu
Mot=ChoixMot(mot) #On choisit un mot
LettresTrouvees=[Mot[0]]#réinitialistation des lettres trouvees
LettresFausses=[]
nbchance = 7 #On réinitialise les essais

#Création de la fenêtre principale
MyWindow=Tk()
MyWindow.title('Le pendu')#Titre de la fenêtre
MyWindow.geometry('480x560+900+150') #Taille de la fenêtre
MyWindow.configure(bg='white') #On change la couleur du fond.
MyWindow.iconbitmap("bonhomme1.gif")

#Creation d'un menu 
menubar= Menu(MyWindow)
menufichier= Menu(menubar,tearoff=0)
menufichier.add_command(label="Rejouer", command= Rejouer)
menufichier.add_command(label="Quitter", command = MyWindow.destroy)
menubar.add_cascade(label="Fichier", menu=menufichier)
MyWindow.config(menu=menubar)

#Importation de toutes les images
image1=PhotoImage(master=MyWindow, file='bonhomme1.gif')
image2=PhotoImage(master=MyWindow, file='bonhomme2.gif')
image3=PhotoImage(master=MyWindow, file='bonhomme3.gif')
image4=PhotoImage(master=MyWindow, file='bonhomme4.gif')
image5=PhotoImage(master=MyWindow, file='bonhomme5.gif')
image6=PhotoImage(master=MyWindow, file='bonhomme6.gif')
image7=PhotoImage(master=MyWindow, file='bonhomme7.gif')
image8=PhotoImage(master=MyWindow, file='bonhomme8.gif')

#Canevas
Largeur=310
Hauteur=320
Canevas=Canvas(MyWindow, height= Hauteur, width=Largeur,bg='grey')
item = Canevas.create_image(150,150,image=image1)

#Entree
lettre_trouvee=StringVar()
ButtonEntree=Entry(MyWindow,textvariable=lettre_trouvee)

#Bouton fermer
ButtonQuitter=Button(MyWindow,text='Quitter',command=MyWindow.destroy)
#Bouton rejouer
ButtonRejouer=Button(MyWindow,text='Rejouer',command=Rejouer)
#Bouton proposer
ButtonProposer=Button(MyWindow,text='Proposer',command = Pendu)




#Affichage mot
mot_affiche=StringVar()
mot_affiche.set(AffichageMot(Mot,LettresTrouvees))
LabelMot_recherche=Label(MyWindow,textvariable=mot_affiche,fg='black',bg='lightgrey')

#Nombre de coups restants
Coups_restants=StringVar()
Coups_restants.set("Il vous reste  " + str(nbchance) + " chances pour gagner !")
LabelCoup=Label(MyWindow,textvariable=Coups_restants,fg='black',bg='lightgrey')

#Lettres fausses
List=StringVar()
Lettres_fausses=Label(MyWindow,textvariable=List,fg='black',bg='lightgrey')

#Affichage
LabelCoup.pack(padx=50,pady=0)
LabelMot_recherche.pack(padx=150,pady=0)
ButtonEntree.pack(padx=150,pady=0)
ButtonProposer.pack(padx=150,pady=0)
ButtonRejouer.pack(padx=150,pady=0)
ButtonQuitter.pack(padx=150,pady=0)
Lettres_fausses.pack(padx=150,pady=0)
Canevas.pack(padx=10,pady=0)


Rejouer()

Mot=Rejouer()[0]
LettresTrouvees=Rejouer()[1]
LettresFausses=Rejouer()[2]
nbchance=Rejouer()[3]

MyWindow.mainloop()