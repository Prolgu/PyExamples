#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Menu.py
#
#  Copyright 2020  Pr0LgU <https://github.com/Prolgu>
#

import os, sys

def menu():

    os.system('clear')
    print("Esto parece un menu:")
    print("\t1 - Primera opcion")
    print("\t2 - Segunda opcion")
    print("\t3 - Tercera opcion")
    print("\tq - Para salir")


def opMenu(a):
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
        exit("Gracias, Vuelva Prontosss.")
    elif a=="q":
        exit("Gracias, Vuelva prontosss")
    else:
        print("")
        input("Ingresa algo del menu.\n")

while True:

    menu()
    opcionMenu = input("Inserta un valor >> ")
    opMenu(opcionMenu)

