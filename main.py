def exercice1(): 
    print("Exercice 1 : Bonjour le monde !") 
    print("Hello World !") 
 
def exercice2():
    prenom=input("Quelle est ton prénom ?")
    print("Bonjour",prenom ,"!")

def exercice3():
    print("premiere ligne")
    print("deuxieme ligne")
    print("troisieme ligne")

def exercice4():
    annee=int(input("Quelle est votre année de naissance ?"))
    print("Vous avez donc :",2025-annee)

def exercice5():
    premier=int(input("quelle est la premier chiffre ?"))
    deuxieme=int(input("quelle est votre deuxieme chiffre ?"))
    print("Le resultat est:",premier+deuxieme)

def exercice6():
    premier=int(input("quelle est la premier chiffre ?"))
    deuxieme=int(input("quelle est votre deuxieme chiffre ?"))
    print("Le resultat est :",premier-deuxieme)

def exercice7():
    premier=int(input("quelle est la premier chiffre ?"))
    deuxieme=int(input("quelle est votre deuxieme chiffre ?"))
    print("Le resultat est :",premier*deuxieme)

def exercice8():
    premier=int(input("quelle est la premier chiffre ?"))
    deuxieme=int(input("quelle est votre deuxieme chiffre ?"))
    print("Le resultat est :",premier/deuxieme)

def exercice9():
    chiffre=int(input("quelle chiffre ?"))
    print("le resultat est :",chiffre**2)

def exercice10():
    chiffre=int(input("quelle est votre chiffre que vous voulez doublé ?  "))
    print("le resultat est :",chiffre*2)

def exercice11():
    chiffre=int(input("Quelle est le chiffre dont vous voulez la moitié ?   "))
    print("le resultat est : ",chiffre/2)

def exercice12():
    for i in range(5):
        print("5")

def exercice13():
    for i in range(5):
        print(i+1) 

def exercice14():
    for i in range(1,6):
        print("2 x",i,"=",i*2)
 
def exercice15():
    cote=int(input("Quelle taille fait le coté ?  "))
    print("Le périmetre est ",cote*4)

def exercice16():
    cote=int(input("Quelle taille fait le coté ?  "))
    print("L'aire des de :",cote*cote)

def exercice17():
    chiffre=int(input("quelle est le prix a convertir ?"))
    print("la converson est de : ",chiffre*1.1)

def exercice18():
    temps=int(input("quelle est le temps a convertir en seconde ?  "))
    print("le resultat est de : ",temps*60)

def exercice19():
    prixHT=int(input("quelle est le prix hors taxe ? "))
    print("le pris TTC est de :",prixHT*1.2)

def exercice20():
    age=int(input("Quelle age as-tu ?  "))
    prenom=input("Quelle est ton prenom ?  ")
    print("Tu t'appelle",prenom,"et tu as",age,"ans")

##NIVEAU BASIQUE##

def exercice21():
    chiffre=int(input("quelle est le chiifre ?  "))
    if chiffre==0:
        print("votre chiffre est nul")
    elif chiffre<0:
        print("Votre chiffre est négatif")
    else:
        print("Votre chiffre est positif")







def main(): 
    # Demande à l'utilisateur quel exercice exécuter 
    choix = input("Entrez le numéro de l'exercice à exécuter : ") 
    if choix == "1": 
        exercice1() 
    elif choix == "2":
        exercice2()
    elif choix == "3":
        exercice3()
    elif choix == "4":
        exercice4()
    elif choix == "5":
        exercice5()
    elif choix == "6":
        exercice6()
    elif choix == "7":
        exercice7()
    elif choix == "8":
        exercice8()
    elif choix == "9":
        exercice9()
    elif choix == "10":
        exercice10()
    elif choix == "11":
        exercice11()
    elif choix == "12":
        exercice12()
    elif choix == "13":
        exercice13()
    elif choix == "14":
        exercice14()
    elif choix == "15":
        exercice15()
    elif choix == "16":
        exercice16()
    elif choix == "17":
        exercice17()
    elif choix == "18":
        exercice18()
    elif choix == "19":
        exercice19()
    elif choix == "20":
        exercice20()
    elif choix == "21":
        exercice21()
    else: 
        print("Exercice non reconnu.") 
if __name__ == "__main__": 
    main() 