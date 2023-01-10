import random #IMPORTIAMO IL MODULO RANDOM CHE CI PERMETTE DI GENERARE UN RANGE DI NUMERI CAUSUALI

while True:
    for x in range(3):
        print("VITE DISPONIBILI:" + str(3-x))
        n = random.randrange(0,10) #GENERIAMO UN NUMERO DA 1 A 10 IN UNA VARIABILE CHIAMATA n
        a = int(input("INSEERISCI UN NUMERO DA 1 A 10: "))#CHIEDIAMO ALL'UTENTE DI INESERIRE UN NUMERO 
        if n == a:#SE IL NUMERO INSERITO È UGUALE A QUELLO GENERATO
         print("GIUSTO, IL NUMERO E' " + str(n) )#STAMPIAMO IL NUMERO CORRETTO INDOVINATO
         print("UNLOCK NEW LEVEL")
         break
 
        if a < 0 or a > 10:#MA SE IL NUMERO È MINORE DI 0 O MAGGIORE DI 10
         print("NUMERO SCELTO NON VALIDO") #STAMPIAMO NUMERO NON VALIDO
        if  n != a and a > 0 and a < 10:#MENTRE SE IL NUMERO INSERITO È DIVERSO DA QUELLO GENERATO
         print("SBAGLIATO, IL NUMERO ESATTO  È "+ str(n))#STAMPIAMO SBAGLIATO, CITANDO IL NUMERO GIUSTO
        if x == 2:
         print("GAME OVER")
    if x == 2 and n != a :
     a = str(input("SE VUOI RIGIOCARE DIGITA 'yes': ")).lower()
    if a != "yes":
      break
