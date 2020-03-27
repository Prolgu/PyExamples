#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Calculos.py
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
# Pide tres valores y devuelve la suma del primero mas el segundo
# y a eso lo multiplica por el tercero


import os

os.system('clear')
input("Escriba tres numeros. ")
os.system('clear')
a=int(input("Ingrese el primero: "))
b=int(input("Ingrese el segundo: "))
c=int(input("Ingrese el tercero: "))

print(f"El resultado es {(a+b)*c} ")


