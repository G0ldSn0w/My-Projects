import random
import time

continu = "y"

while continu == "y":

    while True:
        try:
            dif = int(input("Escull quina dificultat vols \n[1]Facil\n[2]Mitja\n[3]Dificil\n[4]Extrem\n"))
            if dif == 1:
                dificultat = 15
                break
            if dif == 2:
                dificultat = 10
                break
            if dif == 3:
                dificultat = 4
                break
            if dif == 4:
                dificultat = 1
                break
            else:
                print("Sisplau escull un numero entre 1, 2, 3 o 4")
        except:
            print("Sisplau introdueix un numero entre 1, 2, 3 o 4")


    i = 0
    n = random.randint(0,100)
    print("He creat un numero random del 0 - 100, tens " + str(dificultat)  + " intents")

    while i != dificultat:
        a = i + 1
        try:
            nx = int(input("Intent numero " + str(a) + "\n"))
            if nx >= 0 and nx <= 100:
                if nx == n:
                    print("Has guanyat, el numero era " + str(n))
                    break
                elif n > nx:
                    print("El numero random es mes gran que " + str(nx))
                    i = i + 1
                elif n < nx:
                    print("El numero random es mes petit que " + str(nx))
                    i = i + 1
                if i == dificultat:
                    print("Ja no tens mes intents, has perdut \nEl numero random era " + str(n))
        except:
            print("Sisplau introdueix un numero del 0 al 100")
       

    while True:
        restart = (input("Vols tornar a jugar? y/n?\n"))
        if restart == "y":
            continu = restart
            print("Reiniciant...")
            time.sleep(2)
            break
        elif restart == "n":
            print("adeu")
            continu = restart
            break
        else:
            print("sisplau especifica si o no")

        

    


    
    
        
        
    
    
