import subprocess
#Que veut l'utilisateur
user_want = input("Bonjour, bienvenue sur le jeu ChiFouMi developpe par Adrien LEIB, que souhaitez-vous faire ? \n 1 - Jouer en 1VS1 sur console \n 2 - Jouer en 1VSOrdi sur console  \n 3 - Jouer en en 1VSOrdi graphiquement ? \n")

#Un script est lance selon son choix
if(user_want=='1'):
	subprocess.call("python 1vs1_console.py")
elif(user_want=='2'):
	subprocess.call("python 1vsOrdinateur_console.py")
elif(user_want=='3'):
	subprocess.call("python 1vsOrdinateur_graphique.py")
else:
	print("Veuillez saisir un jeu correct")