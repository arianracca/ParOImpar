import random
def checkParImpar(numero):
    x = int(numero) #Casting into integer
    x%=2 #Checking if it's odd or even
    if x == 0:
        par = 2
        print("El número es par!")
        return(par)
    else:
        par = 1
        print("El número es impar!")
        return (par)

def checkApuesta(machine_lives, player_lives, apuesta, par):
    if apuesta == par:
        machine_lives-=1
        return machine_lives
    else:
        player_lives-=1
        return player_lives


player_lives = int(3)
machine_lives = int(3)
player_choice = 0
apuesta = 0
par = 0
open_game = True

while open_game == True & player_lives > 0 & machine_lives > 0:
    num1 = input("Hola! \nElige un número entero para iniciar. (0: Salir)\n")
    if num1 != "0":
        if num1.isdigit(): #Checking if it's an integer
            machine_num = random.randint(1,1000)
            print("Tu adversario eligió: " + machine_num)
            num1 = machine_num + int(num1)
            player_choice = input("Apuesta!\n1.Impar\n2.Par")
            if player_choice == 1 | player_choice == 2:
                checkParImpar(num1)
                checkApuesta(machine_lives,player_lives,player_choice, par)
            else:
                print("Debes ingresar una apuesta válida.\nInténtalo nuevamente.")
        else:
            print("Debes ingresar un número entero.\nInténtalo nuevamente.")
            break
    else:
        print("Hasta la próxima!")
        open_game = False

    if player_lives <= 0:
        print("Perdiste... lo siento.")
    elif machine_lives <=0:
        print("GANASTE!! Felicitaciones.")

    reset = input(print("Deseas jugar nuevamente?\n1.Si\nPresiona cualquier tecla para salir."))
    if reset == 1:
        player_lives = 3
        machine_lives = 3
        player_choice = 0
        apuesta = 0
        par = 0
        open_game = True
    else:
        print("Hasta la próxima!")









