#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Diccionario-For_menu.py
#  
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

