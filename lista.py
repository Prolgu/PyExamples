#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# lista.py
#
# Pr0LgU <https://github.com/Prolgu>
#
lista = [1,2,4,5,1,1]
lista2= [6,7,8]

lista.append(6)#inserta pero so al final
lista.insert(2,3)#inserta en donde se le marca(2 aca)
lista.extend([6,7,8])#extiende desde el final

lista3 =lista+lista2#concatenar
print(lista)
print(len(lista))#largo
print (10 in lista)#existencia o pertenencia(ret. bool)
print(lista.index(5))#busqueda de indice
print(lista.count(10))#contar repeticiones

lista.pop(3)#eliminar(con indice)
lista.remove(1)#elimina buscando el valor
lista.clear()#limpia la lista
lista.reverse()#revierte la lista
lista.sort(reverse=True)#ordena (reversa)



