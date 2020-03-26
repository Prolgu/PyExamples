#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Tabla-Multiplicar.py
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