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

def exercice22():
    age=int(input("Quelle est ton age ?  "))
    if age>=18:
        print("majeur")
    else:
        print("mineur")

def exercice23():
    note=int(input("quelle est votre note ?  "))
    if note>=10:
        print("Tu passes")
    else:
        print("non tu redoubles en sahhhh")

def exercice24():
    chiffre1=int(input("premier chiffre ??  "))
    chiffre2=int(input("deuxieme chiffre ??")) 
    if chiffre1>chiffre2:
        print("le premier plus grand que le deuxieme")
    elif chiffre2>chiffre1:
        print("le deuxieme est plus greand que le chiffre 1")
    else:
        print("les deux sont pareil")

def exercice25():
    c1=int(input("1 quelle est votre chiffre ?"))
    c2=int(input("2 Qelle est votre chiffre"))
    if c1>c2:
        print("les chiffres ne sont pas dans l'ordre croissant")
    else:
        print("les chiffre sont dans l'ordre croissant")

def exercice26():
    chiffre=int(input("quelle est ton chiffre a vérifié si il est divisible par 5 ?"))
    if chiffre%5==0:
        print("votre chiffre est divisible par 5")
    else:
        print("Votre chiffre n'est pas divisible par 5")

def exercice27():
    age=int(input("Quelle est votre age ?  "))
    if age>=18:
        print("vous etes un adulte")
    elif age<=12:
        print("vous etes un enfant")
    else:
        print("vous etes un ado")

def exercice28():
    temperature=int(input("quelle est la temperature de l'eau ?  "))
    if temperature<0:
        print("l'eat est glacé")
    elif temperature>100:
        print("l'eat est en forme gazeuse")
    else:
        print("l'eau est sous forme liquide")

def exercice29():
    note=int(input("quelle est votre notre au bac ?  "))
    if note<10:
        print("vous etes recalé")
    elif 20<note>16:
        print("Vous l'avez avec la mention tres bien")
    elif 10<note<12:
        print("Vous l'avez eu sans mention")
    else:
        print("vous l'avez avec la mention bien")

def exercice30():
    n=int(input("Quelle est votre nombre ?  "))
    for i in range(1,n+1):
        print(i)

def exercice31():
    n=int(input("quelle est votre nombre"))
    for i in range(0,n+1):
        print(n-i)

def exercice32():
    r=0
    n=int(input("Quelle est votre nombre ?  "))
    for i in range(0,n+1):
        r+=i
    print(r)

def exercice33():
    n=int(input("quelle est votre nombre ?  "))
    for i in range(1,11):
        print(n,"x",i,"=",i*n)

def exercice34():
    n=int(input("Quelle est votre nombre ?  "))
    for i in range(1,n+1):
        if i%2==0:
            print(i)

def exercice35():
    n=int(input("quelle est votre nombre ?  "))
    for i in range(1,n+1):
        if i*i<20:
            print(i*i)

def exercice36():
    n=int(input("Quelle est votre nombre ?  "))
    for i in range(1,n+1):
        print("salut")

def exercice37():
    print("  X")
    print(" XXX")
    print("XXXXX")








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
    elif choix == "22":
        exercice22()
    elif choix == "23":
        exercice23()
    elif choix == "24":
        exercice24()
    elif choix == "25":
        exercice25()
    elif choix == "26":
        exercice26()
    elif choix == "27":
        exercice27()
    elif choix == "28":
        exercice28()
    elif choix == "29":
        exercice29()
    elif choix == "30":
        exercice30()
    elif choix == "31":
        exercice31()
    elif choix == "32":
        exercice32()
    elif choix == "33":
        exercice33()
    elif choix == "34":
        exercice34()
    elif choix == "35":
        exercice35()
    elif choix == "36":
        exercice36()
    elif choix == "37":
        exercice37()
    else: 
        print("Exercice non reconnu.") 
if __name__ == "__main__": 
    main() 