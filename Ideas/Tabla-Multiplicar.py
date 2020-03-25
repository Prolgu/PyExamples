#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Menu.py
#
#  Copyright 2020  Pr0LgU <https://github.com/Prolgu>
#

lista = []

salir = False

while not salir:
    numero = int(input("Introduzca un numero: "))
    if numero != 0:
        lista.clear()
        for i in range(0, 11):
            resultado = i * numero
            lista.append(resultado)
        print(lista)
    else:
        print("Adios")
        salir = True