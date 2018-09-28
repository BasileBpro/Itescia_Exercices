from math import *

etat = False
etatDate = False
listeMois = ["janvier", "fevrier", "mars", "avril", "mai", "juin", "juillet", "aout", "septembre", "octobre", "novembre", "decembre"]
listeNovDec = ["novembre", "decembre"]
listePair=["avril","juin","septembre","novembre"]
date = input("Quel jour souhaitez vous connaître sous la forme \'5 fevrier 2018\'")
def verifDate(date):
    listeDate = date.split(" ")
    if(listeDate[1] in listeMois):
        print("Le mois est bon")
        if(int(listeDate[0])>0 and int(listeDate[0])<32):
            print("Le jour est bon")
            if(int(listeDate[2])>=1582):
                print("L'année est bonne")
                etatDate = True
            else:
                 etatDate = False
        else:
            etatDate = False
    else:
        etatDate = False
    if(int(listeDate[2]) == 1582 and etatDate):
        if(listeDate[1] in listeNovDec):
            etatDate = True
        else:
            etatDate = False
    if(etatDate and listeDate[1] in listePair):
        if(int(listeDate[0])>30):
            etatDate = False
    if(etatDate and listeDate[1]=="fevrier"):
        if(int(listeDate[2]) % 4 == 0 and int(listeDate[2]) % 100 != 0 and int(listeDate[0]) < 30):
            etatDate = True
        elif(int(listeDate[2]) % 4 != 0 and int(listeDate[2]) % 100 == 0 and int(listeDate[0]) < 29):
            etatDate = True
        else :
            etatDate = False
    if(etatDate):
        return True
    else:
        return False

while etat!=True:
    if verifDate(date)==False:
        date = input("Veuillez ne pas mettre d'accent ou de majuscule, n'oubliez pas les espaces et insérer une date valide après le 1 novembre 1582")
    else :
        etat = True
somme = 0

 #date = input("Quel jour souhaitez vous connaître sous la forme \'5 fevrier 2018\'")


# Recupération des deux derniers chiffres de l'année
def RecupChiffreAnnee():
    listeDate = date.split(" ")
    global somme
    somme += int(listeDate[2][2:4])
    return listeDate[2][2:4]


# Ajout du quart des deux derniers chiffres de l'année
def AjoutQuart():
    global somme
    somme += floor(int(RecupChiffreAnnee()) / 4)
    return floor(int(RecupChiffreAnnee()) / 4)


# On rajoute le jour à la somme
def AjoutJour():
    AjoutQuart()
    global somme
    somme += int(date.split(" ")[0])


# On rajoute à la somme le nombre correspondant au mois
def Mois():
    AjoutJour()
    listeDate = date.split(" ")
    global somme
    if listeDate[1] == 'janvier' or listeDate[1] == 'octobre':
        somme += 0
    elif listeDate[1] == 'fevrier' or listeDate[1] == 'mars' or listeDate[1] == 'novembre':
        somme += 3
    elif listeDate[1] == 'avril' or listeDate[1] == 'juillet':
        somme += 6
    elif listeDate[1] == 'juin':
        somme += 4
    elif listeDate[1] == 'mai':
        somme += 1
    elif listeDate[1] == 'decembre' or listeDate[1] == 'septembre':
        somme += 5
    elif listeDate[1] == 'aout':
        somme += 2


# On vérifie si l'année est bissextile ou non
def bissextile():
    Mois()
    listeDate = date.split(" ")
    global somme
    if (int(listeDate[2]) % 4 == 0 and int(listeDate[2]) % 100 != 0 and listeDate[1] == 'janvier') or (
            int(listeDate[2]) % 4 == 0 and int(listeDate[2]) % 100 != 0 and listeDate[1] == 'fevrier'):
        somme -= 1


# On rajoute à la somme le nombre correspondant au siècle
def Siecle():
    bissextile()
    listeDate = date.split(" ")
    global somme
    if listeDate[2][0:2] == "16" or listeDate[2][0:2] == "20":
        somme += 6
    elif listeDate[2][0:2] == "17" or listeDate[2][0:2] == "21":
        somme += 4
    elif listeDate[2][0:2] == "18" or listeDate[2][0:2] == "22":
        somme += 2
    elif listeDate[2][0:2] == "19" or listeDate[2][0:2] == "23":
        somme += 0


# On récupère ensuite le jour final selon le chiffre final
def JourFinal():
    Siecle()
    global somme
    somme = somme % 7
    jour = ""
    if somme == 0:
        jour = "dimanche"
    elif somme == 1:
        jour = "lundi"
    elif somme == 2:
        jour = 'mardi'
    elif somme == 3:
        jour = 'mercredi'
    elif somme == 4:
        jour = 'jeudi'
    elif somme == 5:
        jour = 'vendredi'
    elif somme == 6:
        jour = 'samedi'
    return jour


# On affiche le jour
print("Le " + date + " était un " + JourFinal())
