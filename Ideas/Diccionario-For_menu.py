#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Diccionario-For.py
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
import os

salir = False
dic={'1': '0', '2': '0', '3': '0', '4': '0'}#defino mi diccionario

def menu():                         #mi memu principal
    os.system('clear')
    print("Esto parece un menu:")
    print("\t1 - Ingresar valores")
    print("\t2 - Leer valores")
    print("\tq - Para salir")
    
def ingreso():
    os.system('clear')              #limpio
    for key in dic.keys():          #Bucle de ingreso
        dic[key]=input(f"Valor[{key}]: ") #repito hasta ingresar un dato  por cada entrada del diccionario

def imprimo():
    os.system('clear')              #limpio
    print("Ingresaste estos valores:")
    for key in dic.keys():          #bucle de impresion
        print(key, "->",dic[key])   #Imprimo 
        
#def menu_salida():

while not salir:
    menu()

    a = input("Inserta un valor >> ")
    if a=="1":
        ingreso()
        input("\nPresiona una tecla para continuar.")
    elif a=="2":
        imprimo()
        input("\nPresiona una tecla para continuar.")
    elif a=="q":
        salida = False
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
                input("Ingresa algo del menu.")
    else:
        print("")
        input("Ingresa algo del menu.\n")

