#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
<<<<<<< HEAD
#  Menu.py
#
#   2020  Pr0LgU <https://github.com/Prolgu>
#
=======
#  Calcu.py
#  
#  Pr0LgU <https://github.com/Prolgu>
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

>>>>>>> c2ae83f1dd54fdc3632f52bfb7619277c5a71738
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
	


