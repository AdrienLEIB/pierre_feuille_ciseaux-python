import random
import os 
import time

#Petit effacement de console pour que ça soit jolie
os.system("cls")

#On definit les scores
score_utilisateur = 0
score_utilisateur2 = 0

#Touche joueur 1
print("Joueur 1 - Definissez vos touches");
utilisateurPierre = input("Choissiez la touche pour Pierre \n")
#On evite qu'il est les memes touches
while True:
    utilisateurFeuille = input("Choissiez la touche pour Feuille \n")
    if(utilisateurFeuille != utilisateurPierre):
        break
while True:
    utilisateurCiseaux = input("Choissiez la touche pour Ciseaux \n")
    if(utilisateurCiseaux!= utilisateurPierre) and (utilisateurCiseaux != utilisateurFeuille):
        break

#On supprime la console pour pas que le joueur 2 voit
os.system("cls")

#Touche joueur 2
print("Joueur 2 - Definissez vos touches");
utilisateur2Pierre = input("Choissiez la touche pour Pierre \n")
while True:
    utilisateur2Feuille = input("Choissiez la touche pour Feuille \n")
    if(utilisateur2Feuille!=utilisateurPierre):
        break
while True:
    utilisateur2Ciseaux = input("Choissiez la touche pour Ciseaux \n")
    if(utilisateur2Ciseaux!= utilisateur2Pierre) and (utilisateur2Ciseaux != utilisateur2Feuille):
        break

#Tant qu'aucun des des joueurs n'a pas au moins 2 points
while (score_utilisateur!=2) and (score_utilisateur2!=2):

    #Joueur 1 indique son coup
    utilisateur_coup= input("Joueur 1 - Pierre, Feuille ou Ciseaux? (noubliez pas vos touches)\n")

    #J'avais la flemme de changer toutes les valeurs de chaque if par utilisateurPierre,utilisateurFeuille et utilisateurCiseaux
    if utilisateur_coup == utilisateurPierre:
        utilisateur_coup = "pierre"
    elif utilisateur_coup == utilisateurFeuille:
        utilisateur_coup = "feuille"        
    elif utilisateur_coup == utilisateurCiseaux:
        utilisateur_coup = "ciseaux"

    os.system("cls")

    #Joueur  2 indique son coup 
    utilisateur2_coup= input("Joueur 2 - Pierre, Feuille ou Ciseaux? (noubliez pas vos touches)\n")
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
        print("Le joueur 1 a joue pierre,\n Le joueur 2 ciseaux, \n ", score_utilisateur," - ", score_utilisateur2)
        

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
    
    
#Qui a gagne?
if score_utilisateur == 2:
    print("Joueur 2 a gagne !")
elif score_utilisateur2 == 2:
    print("Joueur 1 a gagne ! ")
