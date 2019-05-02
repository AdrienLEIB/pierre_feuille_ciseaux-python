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

    #Pierre
    if utilisateur_coup == "pierre" and utilisateur2_coup == "ciseaux":
        score_utilisateur= score_utilisateur + 1
        print("Le joueur 2 a joue ciseaux, Le joueur 1 pierre, le joueur 1 remporte cette manche le score est donc de :", score_utilisateur," - ", score_utilisateur2)
        

    elif utilisateur_coup =="pierre" and utilisateur2_coup =="pierre":
        print("Les joueurs 2 et 1 ont joues pierre, egalite sur cette manche le score est donc de :", score_utilisateur," - ", score_utilisateur2)

    elif utilisateur_coup =="pierre" and utilisateur2_coup == "feuille":
        score_utilisateur2 = score_utilisateur2 +1
        print("Le joueur 1 a joue feuille, le joueur 1 a joue pierre, le joueur 2 remporte cette manche le score est donc de :", score_utilisateur," - ", score_utilisateur2)

    #Ciseaux
    elif utilisateur_coup =="ciseaux" and utilisateur2_coup == "ciseaux":
        print("Les 2 joueurs ont joue ciseaux, egalite sur cette manche le score est donc de :", score_utilisateur," - ", score_utilisateur2)
    elif utilisateur_coup =="ciseaux" and utilisateur2_coup =="pierre":
        score_utilisateur2 = score_utilisateur2 +1
        print("Joueur 2 a joue pierre, Joueur 1 ciseaux, le joueur 2 gagne cette manche le score est donc de :", score_utilisateur," - ", score_utilisateur2)
    elif utilisateur_coup == "ciseaux" and utilisateur2_coup == "feuille":
        score_utilisateur= score_utilisateur + 1
        print("Joueur 2 a joue feuilleet le joueur 1 ciseaux, le joueur 1 remporte cette manche le score est donc de :", score_utilisateur," - ", score_utilisateur2)

    #Feuille
    elif utilisateur_coup == "feuille" and utilisateur2_coup == "ciseaux":
        score_utilisateur2= score_utilisateur2 + 1
        print("Le joueur 2 a joue ciseaux, le joueur 1 a joue feuille,le joueur 2 remporte cette manche le score est donc de :", score_utilisateur," - ", score_utilisateur2)
    elif utilisateur_coup == "feuille" and utilisateur2_coup == "pierre":
        score_utilisateur = score_utilisateur +1
        print("Le joueur 2 a joue pierre et le joueur 1 feuille, le joueur 1 remporte cette manche le score est donc de :", score_utilisateur," - ", score_utilisateur2)
    elif utilisateur_coup =="feuille" and utilisateur2_coup == "feuille":
        print("Le joueur 1 et 2 ont joues feuille, egalite sur cette manche le score est donc de :", score_utilisateur," - ", score_utilisateur2)
    print("")
    
    

if score_utilisateur == 2:
    print("Joueur 2 a gagne !")
elif score_utilisateur2 == 2:
    print("Joueur 1 a gagne ! ")
