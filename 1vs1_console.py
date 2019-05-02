import random
import os 
import time

os.system("cls")
score_utilisateur = 0
score_utilisateur2 = 0
print("Joueur 1 - Definissez vos touches");
utilisateurPierre = input("Choissiez la touche pour Pierre \n")
utilisateurFeuille = input("Choissiez la touche pour Feuille \n")
utilisateurCiseaux = input("Choissiez la touche pour Ciseaux \n")

os.system("cls")
print("Joueur 2 - Definissez vos touches");
utilisateur2Pierre = input("Choissiez la touche pour Pierre \n")
utilisateur2Feuille = input("Choissiez la touche pour Feuille \n")
utilisateur2Ciseaux = input("Choissiez la touche pour Ciseaux \n")

while (score_utilisateur!=2) and (score_utilisateur2!=2):
    utilisateur_coup= input("Joueur 1 - Pierre, Feuille ou Ciseaux? ecrire tous en minuscule \n")

    if utilisateur_coup == utilisateurPierre:
        utilisateur_coup = "pierre"
    elif utilisateur_coup == utilisateurFeuille:
        utilisateur_coup = "feuille"        
    elif utilisateur_coup == utilisateurCiseaux:
        utilisateur_coup = "ciseaux"

    os.system("cls")

    utilisateur2_coup= input("Joueur 2 - Pierre, Feuille ou Ciseaux? ecrire tous en minuscule \n")
    print("")
    if utilisateur2_coup == utilisateur2Pierre:
        utilisateur2_coup = "pierre"
    elif utilisateur2_coup == utilisateur2Feuille:
        utilisateur2_coup = "feuille"       
    elif utilisateur2_coup == utilisateur2Ciseaux:
        utilisateur2_coup = "ciseaux"
    

    #Si les joueurs entrent une chaine de caractère differente
    if (utilisateur_coup != "pierre" and utilisateur_coup != "feuille" and utilisateur_coup != "ciseaux") or (utilisateur2_coup != "pierre" and utilisateur2_coup != "feuille" and utilisateur2_coup != "ciseaux"):
        print("Un des deux joueurs a saisie une mauvaise touche")
        continue

    #Comparatif pierre user1
    if utilisateur_coup == "pierre" and utilisateur2_coup == "ciseaux":
        score_utilisateur= score_utilisateur + 1
        print("Le joueur 2 a joue ciseaux, \n Le joueur 1 pierre, \n ", score_utilisateur," - ", score_utilisateur2)
        

    elif utilisateur_coup =="pierre" and utilisateur2_coup =="pierre":
        print("Le joueur 1 a joue pierre, \n Le joueur 2 pierre \n", score_utilisateur," - ", score_utilisateur2)

    elif utilisateur_coup =="pierre" and utilisateur2_coup == "feuille":
        score_utilisateur2 = score_utilisateur2 +1
        print("Le joueur 1 a joue pierre, \n le joueur 2 a joue feuille :", score_utilisateur," - ", score_utilisateur2)

    #Comparatif ciseaux user1
    elif utilisateur_coup =="ciseaux" and utilisateur2_coup == "ciseaux":
        print("Le joueur 1 a joue ciseaux, \n le joueur 2 a joue ciseaux :", score_utilisateur," - ", score_utilisateur2)
    elif utilisateur_coup =="ciseaux" and utilisateur2_coup =="pierre":
        score_utilisateur2 = score_utilisateur2 +1
        print("Le joueur 1 a joue ciseaux, \n le jouer 2 a joue pierre:", score_utilisateur," - ", score_utilisateur2)
    elif utilisateur_coup == "ciseaux" and utilisateur2_coup == "feuille":
        score_utilisateur= score_utilisateur + 1
        print("Le joueur 1 a joue ciseaux, \n le joueur 2 a joue feuille", score_utilisateur," - ", score_utilisateur2)

    #Comparatif feuille user1
    elif utilisateur_coup == "feuille" and utilisateur2_coup == "ciseaux":
        score_utilisateur2= score_utilisateur2 + 1
        print("Le joueur 1 a joue feuille, \n le joueur 2 a joue ciseaux:", score_utilisateur," - ", score_utilisateur2)
    elif utilisateur_coup == "feuille" and utilisateur2_coup == "pierre":
        score_utilisateur = score_utilisateur +1
        print("Le joueur 1 a joue feuille, \n le joueur 2 a joue pierre :", score_utilisateur," - ", score_utilisateur2)
    elif utilisateur_coup =="feuille" and utilisateur2_coup == "feuille":
        print("Le joueur 1 a joue feuille, \n le joueur 2 a joue feuille :", score_utilisateur," - ", score_utilisateur2)
    print("")
    
    

if score_utilisateur == 2:
    print("Joueur 2 a gagne !")
elif score_utilisateur2 == 2:
    print("Joueur 1 a gagne ! ")
