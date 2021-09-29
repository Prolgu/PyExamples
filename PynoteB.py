#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Pynote.py
# Script para tomar notas simples
#
# Pr0LgU <https://github.com/Prolgu>



import os
from time import strftime

#variables utiles para el programa
fecha=strftime("%d-%b-%Y")
hora=strftime("* (%H:%M) ")
lineas = []

os.system('clear')

def main():
    #bucle para escribir, se sale con linea vacia y enter.
    while True:
        s = input("\033[1;34m ==> \033[0;m")
        if s:
            lineas.append(hora+s)
        else:
            break;

    #conversion de lista en varias lineas con salto
    procesado="\n".join(lineas)

    with open("log.md","a") as file:
        file.write(f"\n#### {fecha} \n")
        file.write(procesado)        
        # file.write(f"\n========== {horarioB} ==========\n")
        file.close()

if __name__ == '__main__':
    main()
