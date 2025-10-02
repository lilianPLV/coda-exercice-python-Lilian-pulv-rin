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
    else: 
        print("Exercice non reconnu.") 
if __name__ == "__main__": 
    main() 