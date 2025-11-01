import random


    
while True:
    Numero=random.randint(1,10)
    print("Adivina en que numero pienso\n (Mi numero esta del 1 al 10)")
    try:
        Adivinar=int(input(""))
    except ValueError:
         print("Ingrese solo numeros porfavor")
         continue
    if Adivinar>Numero:
            print("Tu numero es mayor a mi numero")
    elif Adivinar<Numero:
            print("Tu numero es menor a mi numero ")
    if Adivinar!=Numero:
        print("Perdiste...")
        print("¿Quieres seguir?")
        seguir=(input(""))
       
       
        if seguir.lower()=="si":
            print("Esoooo, Sin rendirse!!")
            continue
        elif seguir.lower()=="no":
            print("Nos vemos...")
            break
        else:
            print("Valor incorrecto, Solo responde con Si o No...Reinicio del juego")
            continue
    if Adivinar==Numero:
        print("Felicidades...Adivinaste el numero :))")
        break
