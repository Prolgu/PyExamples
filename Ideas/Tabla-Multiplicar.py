#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Menu.py
#
#  2020  Pr0LgU <https://github.com/Prolgu>
#

listado = []

salida = False

while not salida:
    numero = int(input("Introduzca un numero: "))
    if numero != 0:
        listado.clear()
        for i in range(0, 11):
            resultado = i * numero
            listado.append(resultado)
        print(listado)
    else:
        print("Adios")
        salida = True