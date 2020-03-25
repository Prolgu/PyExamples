#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Menu.py
#
#  Copyright 2020  Pr0LgU <https://github.com/Prolgu>
#
import os, sys

def menuCalc():

    os.system('clear')
    print("Esto parece un menu:")
    print("\t1 - Suma")
    print("\t2 - Resta")
    print("\t3 - Multiplicacion")
    print("\t4 - Division")
    print("\tq - Para salir")
    
def calculadora(calcu,):
	if calcu == "1":
		os.system('clear')
		s1=int(input("Ingrese un numero\n"))
		s2=int(input("Ingrese otro\n"))
		os.system('clear')
		print(f"{s1} + {s2} = {s1+s2}")
		input("\nPresione una tecla para continuar.")
	elif calcu == "2":
		os.system('clear')
		s1=int(input("Ingrese un numero\n"))
		s2=int(input("Ingrese otro\n"))
		os.system('clear')
		print(f"{s1} - {s2} = {s1-s2}")
		input("\nPresione una tecla para continuar.")
	elif calcu == "3":
		os.system('clear')
		s1=int(input("Ingrese un numero\n"))
		s2=int(input("Ingrese otro\n"))
		os.system('clear')
		print(f" {s1} x {s2} = {s1*s2}")
		input("\nPresione una tecla para continuar.")
	elif calcu == "4":
		os.system('clear')
		s1=int(input("Ingrese un numero\n"))
		s2=int(input("Ingrese otro\n"))
		os.system('clear')
		print(f"{s1} / {s2} = {s1 / s2}")
		input("\nPresione una tecla para continuar.")
	elif calcu == "q":
		print("Gracias, Vuelva Prontoss")
		exit()
	else:
		os.system('clear')
		print("Lo siento no es un numero valido!")

while True:
    
    menuCalc()
    calc = input("Ingrese su opcion: ")
    calculadora(calc)
	


