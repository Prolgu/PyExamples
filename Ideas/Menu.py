#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Menu.py
#  
#  2020 Pr0LgU <https://github.com/Prolgu>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
# 
import os, sys
salir = False

def menu():

    os.system('clear')
    print("Esto parece un menu:")
    print("\t1 - Primera opcion")
    print("\t2 - Segunda opcion")
    print("\t3 - Tercera opcion")
    print("\tq - Para salir")

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
        salida = False
        while not salida:
            os.system('clear')
            b = input("Desea salir?\n1 - Si.\n2 - No.\n")
            if b=="1":
                salir1 = True
            elif b=="2":
                os.system('clear')
                salida = True
            else:
                print("")
                input("Ingresa algo del menu.\n")   
    else:
        print("")
        input("Ingresa algo del menu.\n")

