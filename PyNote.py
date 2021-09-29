#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# PyNote.py
# script de anotaciones de una linea
# Pr0LgU <https://github.com/Prolgu
#
import os
from time import strftime

horario=strftime("%d.%b.%Y (%H:%M)")
salir=0
l_cnt = 1

os.system('clear')
print(" (1) Escribe (2) Consulta  U.L. (3) Imprime todo (4) Salida")

def doLinea(a):
    if a==1:
        # creacion/anexado de lineas
        with open('log','a') as f:
            logg=input("\033[1;34m ->> \033[0;m")
            f.write(f"{l_cnt} -> {horario} {logg}.\n")
            f.close()
    elif a==2:
        # lectura de ultima linea
        with open('log','r') as f:
            lineas = f.read().splitlines()  # convertimos en una lista de lineas
            ultima_linea = lineas[-1]   
            f.close()
            print(ultima_linea)
    elif a==3:
        # impresion de todo el archivo
        with open('log','r') as f:
            for x in f:
                print(x) 








def escribirLinea():
    with open('log','a') as f:
        logg=input("\033[1;34m ->> \033[0;m")
        f.write(f"{l_cnt} -> {horario} {logg}.\n")
        f.close()

def ultimaLinea():
    with open('log','r') as f:
        lineas = f.read().splitlines()  # convertimos en una lista de lineas
        ultima_linea = lineas[-1]   
        f.close()
        print(ultima_linea)

def imprimirTodo():
    with open('log','r') as f:
        for x in f:
            print(x) 

if __name__ == '__main__':
    if os.path.exists('log')==True:
        with open('log','r') as f:
            for line in f:
                if line != "\n":
                    l_cnt += 1
            f.close()
    else:
        with open('log','a') as f:
            f.write(f"{l_cnt} -> {horario} Linea Origen.\n")
            f.close()
        l_cnt+=1

    while not salir:
        mnu=input("\033[1;34m ==> \033[0;m")

        if mnu=="1":
            os.system('clear')
            escribirLinea()
            l_cnt+=1
        elif mnu=="2":
            ultimaLinea()
        elif mnu=="3":
            imprimirTodo()
        elif mnu=="4" or "q":
            salir=1
            break
        else:
            print("Error.")

# if __name__ == "__main__":
#     main()
