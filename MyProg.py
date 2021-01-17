#def myfunct():
#    while True:
 #       myWords = input("How are you today? ")
  #      if myWords == "Fine":
  #          print("Good for you!")
  #          break
   #     elif myWords == "Bad":
  #          print("Sorry to hear that")
   #         break
   #     else:
  #          print("What?")
   #         pass

def saisieNum(invite):
    while True:
        myNum = int(input(invite))
        if myNum == False:
            print("Veuillez entrer un nombre et pas autre chose SVP!")
            pass
        else:
            return myNum

def randIntGen(a, b):
    import random
    randNum = random.randint(a, b)
    return randNum

def helpQuestion():
    while True:
        helpansw = input("Voulez-vous afficher les limites révisées après chaque tentative pour mieux visualiser où vous en êtes? Y/N : ")
        try:
            helpansw == "Y" or helpansw == "N"
            break
        except:
            pass
        return helpansw

#def limiter(helpansw):
#    if helpansw == "Y":
#        print("Les limites actuelles sont: Min = " + str(infL) + " Max = " + str(supL))
    

def difficultyLevel():
    inf = 1
    answ = int(input("""Vous pouvez choisir un niveau de difficulté parmis les suivants:
- 1 : débutant (1-20)
- 2 : initié (1-100)
- 3 : confirmé (1-10000)
- 4 : expert (1-1000000)
- 5 : custom (vous choisissez les limites)
Si vous tapez autre chose, le niveau par défaut est 'initié'.
Entrez ici votre choix: """))
    if answ == 1:
        sup = 20
    elif answ == 2:
        sup = 100
    elif answ == 3:
        sup = 10000
    elif answ == 4:
        sup = 1000000
    elif answ == 5:
        inf = saisieNum("Veuillez entrer la limite inférieure: ")
        sup = saisieNum("Veuillez entrer la limite supérieure: ")
    else:
        inf = 1
        sup = 100
    return(inf, sup)

#inf = saisieNum("Veuillez entrer la limite inférieure pour le jeu: ")
#sup = saisieNum("Veuillez entrer la limite supérieure pour le jeu: ")
def myGame():
    inf, sup = difficultyLevel()
#    helpansw = helpQuestion()
    myRand = randIntGen(inf, sup)
    count, infL, supL = 1, inf, sup
    while True:
        guess = saisieNum("Votre nombre? ")
        if guess == myRand:
            print("Gagné!")
            print("Vous avez mis " + str(count) + " essais.")
            break
        elif guess < inf:
            count = count + 1
            print("Vous êtes en-dessous de la limite, qui a été définie comme " + str(inf))
            pass
        elif guess < myRand:
            count = count +1
            infL = myRand
            print("Trop bas!")
            pass
        elif guess > sup:
            count = count + 1
            print("Vous êtes au-dessus de la limite, qui a été définie comme " + str(sup))
            pass
        else:
            count = count + 1
            supL = myRand
            print("Trop haut!")
            pass

myGame()
