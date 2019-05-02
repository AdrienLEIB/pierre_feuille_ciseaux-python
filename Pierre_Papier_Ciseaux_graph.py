from tkinter import *
import random
from tkinter.messagebox import*

score_ordinateur = 0
score_utilisateur = 0

def ciseaux():
    global score_ordinateur
    global score_utilisateur
    ordinateur_coup= random.randint(1,3)
    pierre = 1 #pierre prends la valeur 1
    feuille = 2 #feuille prends la valeur 2
    ciseaux = 3 #ciseaux prends la valeur 3
    if(ordinateur_coup==pierre):
        score_ordinateur = score_ordinateur +1
        print("L'ordinateur a joue pierre, vous perdez cette manche le score est donc de :", score_utilisateur," - ", score_ordinateur)
    elif(ordinateur_coup==ciseaux):
        print("L'ordinateur a joue ciseaux, egalite sur cette manche le score est donc de :", score_utilisateur," - ", score_ordinateur)
    elif(ordinateur_coup==feuille):
        score_utilisateur= score_utilisateur + 1
        print("L'ordinateur a joue feuille, vous remportez cette manche le score est donc de :", score_utilisateur," - ", score_ordinateur)
    ScoreUti.config(text=score_utilisateur)
    ScoreOrdi.config(text=score_ordinateur)    
    resultat()

def pierre():
    global score_utilisateur
    global score_ordinateur
    ordinateur_coup= random.randint(1,3)
    pierre = 1 #pierre prends la valeur 1
    feuille = 2 #feuille prends la valeur 2
    ciseaux = 3 #ciseaux prends la valeur 3
    if(ordinateur_coup==pierre):
        print("L'ordinateur a joue pierre, egalite sur cette manche le score est donc de :", score_utilisateur," - ", score_ordinateur)
    elif(ordinateur_coup==ciseaux):
        score_utilisateur = score_utilisateur+1
        print("L'ordinateur a joue ciseaux, vous perdez cette manche le score est donc de :", score_utilisateur," - ", score_ordinateur)
    elif(ordinateur_coup==feuille):
        score_ordinateur= score_ordinateur + 1
        print("L'ordinateur a joue feuille, vous perder cette manche le score est donc de :", score_utilisateur," - ", score_ordinateur)
    ScoreUti.config(text=score_utilisateur)
    ScoreOrdi.config(text=score_ordinateur)
    resultat()

def feuille():
    global score_utilisateur
    global score_ordinateur
    ordinateur_coup= random.randint(1,3)
    pierre = 1 #pierre prends la valeur 1
    feuille = 2 #feuille prends la valeur 2
    ciseaux = 3 #ciseaux prends la valeur 3
    if ordinateur_coup == ciseaux:
        score_ordinateur= score_ordinateur + 1
        print("L'ordinateur a joue ciseaux, vos perdez  cette manche le score est donc de :", score_utilisateur," - ", score_ordinateur)
    elif ordinateur_coup ==pierre:
        score_utilisateur = score_utilisateur +1

        print("L'ordinateur a joue pierre, vous remportez cette manche le score est donc de :", score_utilisateur," - ", score_ordinateur)
    elif ordinateur_coup == feuille:
        print("L'ordinateur a joue feuille, egalite sur cette manche le score est donc de :", score_utilisateur," - ", score_ordinateur)
    ScoreUti.config(text=score_utilisateur)
    ScoreOrdi.config(text=score_ordinateur)
    resultat()

def resultat():
    global score_ordinateur
    global score_utilisateur
        

    ordinateur_coup= random.randint(1,3)
    pierre = 1 #pierre prends la valeur 1
    feuille = 2 #feuille prends la valeur 2
    ciseaux = 3 #ciseaux prends la valeur 3
    if score_utilisateur == 2:
        print("Bravo vous avez remportez le pierre, feuille, ciseaux !")
        Mafenetre.quit()
    elif score_ordinateur == 2:
        print("Dommage...Vous avez perdu :( ")
        Mafenetre.quit()




Mafenetre = Tk()
Mafenetre.title('Pierre Papier ciseaux')

feuilleimg= PhotoImage(file='papier.gif')
pierreimg= PhotoImage(file='pierre.gif')
ciseauximg= PhotoImage(file='ciseaux.gif')


Largeur = 0
Hauteur = 0
Canevas = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg = "white")
Canevas.pack(padx =100, pady =100)

ScoreUti = Label(Mafenetre, text=score_utilisateur, bg = "white")
ScoreUti.pack()
Score = Label(Mafenetre,  text="-", bg = "white")
Score.pack()
ScoreOrdi = Label(Mafenetre, text=score_ordinateur, bg = "white")
ScoreOrdi.pack()



Pierre = Button(Mafenetre, text ='Pierre', command=pierre)
Pierre.configure(image=pierreimg)
Pierre.pack(side = LEFT, padx = 50, pady = 50)


Feuille = Button(Mafenetre, text ='Feuille', command=feuille)
Feuille.configure(image=feuilleimg)
Feuille.pack(side = LEFT, padx = 50, pady = 50)


Ciseaux = Button(Mafenetre, text ='Ciseaux', command =ciseaux)
Ciseaux.configure(image=ciseauximg)
Ciseaux.pack(side = LEFT, padx = 50, pady = 50)




Mafenetre.mainloop()