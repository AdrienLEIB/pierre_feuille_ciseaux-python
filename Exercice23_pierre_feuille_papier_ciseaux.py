import random


score_utilisateur = 0
score_ordinateur = 0

while (score_utilisateur!=10) and (score_ordinateur!=10):

    #Variable
    ordinateur_coup= random.randint(1,3)
    pierre = 1 #pierre prends la valeur 1
    feuille = 2 #feuille prends la valeur 2
    ciseaux = 3 #ciseaux prends la valeur 3

    utilisateur_coup= input("Pierre, Feuille ou Ciseaux? écrire tous en minuscule \n")
    print("")

    #Si l'utilisateur entre une chaine de caractère différente
    if utilisateur_coup != "pierre" and utilisateur_coup != "feuille" and utilisateur_coup != "ciseaux":
        print("Vous n'avez pas écris correctement : pierre, papier ou ciseaux. Réssayez")

    #Pierre
    if utilisateur_coup == "pierre" and ordinateur_coup == ciseaux:
        score_utilisateur= score_utilisateur + 1
        print("L'ordinateur à joué ciseaux, vous remportez cette manche le score est donc de :", score_utilisateur," - ", score_ordinateur)
        

    elif utilisateur_coup =="pierre" and ordinateur_coup ==pierre:
        print("L'ordinateur à joué pierre, égalité sur cette manche le score est donc de :", score_utilisateur," - ", score_ordinateur)

    elif utilisateur_coup =="pierre" and ordinateur_coup == feuille:
        score_ordinateur = score_ordinateur +1
        print("L'ordinateur à joué feuille, vous perdez cette manche le score est donc de :", score_utilisateur," - ", score_ordinateur)

    #Ciseaux
    elif utilisateur_coup =="ciseaux" and ordinateur_coup == ciseaux:
        print("L'ordinateur à joué ciseaux, égalité sur cette manche le score est donc de :", score_utilisateur," - ", score_ordinateur)
    elif utilisateur_coup =="ciseaux" and ordinateur_coup ==pierre:
        score_ordinateur = score_ordinateur +1
        print("L'ordinateur à joué pierre, vous perdez cette manche le score est donc de :", score_utilisateur," - ", score_ordinateur)
    elif utilisateur_coup == "ciseaux" and ordinateur_coup == feuille:
        score_utilisateur= score_utilisateur + 1
        print("L'ordinateur à joué feuille, vous remportez cette manche le score est donc de :", score_utilisateur," - ", score_ordinateur)

    #Feuille
    elif utilisateur_coup == "feuille" and ordinateur_coup == ciseaux:
        score_utilisateur= score_utilisateur + 1
        print("L'ordinateur à joué ciseaux, vos remportez cette manche le score est donc de :", score_utilisateur," - ", score_ordinateur)
    elif utilisateur_coup == "feuille" and ordinateur_coup ==pierre:
        score_ordinateur = score_ordinateur +1
        print("L'ordinateur à joué pierre, vous perdez cette manche le score est donc de :", score_utilisateur," - ", score_ordinateur)
    elif utilisateur_coup =="feuille" and ordinateur_coup == feuille:
        print("L'ordinateur à joué feuille, égalité sur cette manche le score est donc de :", score_utilisateur," - ", score_ordinateur)
    print("")
    
    

if score_utilisateur == 3:
    print("Bravo vous avez remportez le pierre, feuille, ciseaux !")
elif score_ordinateur == 3:
    print("Dommage...Vous avez perdu :( ")
