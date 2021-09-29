#  

import os
salir = False
def menu():

    os.system('clear')
    print("Esto parece un menu:")
    print("\t1 - Primera opcion")
    print("\t2 - Segunda opcion")
    print("\t3 - Tercera opcion")
    print("\tq - Para salir")
    return

while not salir:

    menu()
    
    a = input("Inserta un valor >> ")
    if a=="1":
        print("Esta es la opcion uno")
        input("\nPresiona una tecla para continuar.")
    elif a=="2":
        print("Esta es la opcion dos")
        input("\nPresiona una tecla para continuar.")
    elif a=="3":
        print("Esta es la opcion tres")
        input("\nPresiona una tecla para continuar.")
    elif a=="4":
        print("Gracias, Vuelva Prontosss.")
        salir = True
    elif a=="q":
        salida=False
        while not salida:
            os.system('clear')
            b = input("Desea salir?\n1 - Si.\n2 - No.\n")
            if b=="1":
                salir = True
                os.system('clear')
                break
            elif b=="2":
                os.system('clear')
                salida = True
                
            else:
                print("")
                input("Ingresa algo del menu.\n")   
    else:
        print("")
        input("Ingresa algo del menu.\n")

