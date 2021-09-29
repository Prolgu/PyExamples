#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  fuzzer.py
#  
#  
#  
#  


import random

numStri="1234567890"
letStriA="abcdefghijklmnopqrstuvwxyz"
letStriB="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letSymbo="~!@#$%^&*()_+{}|:/;=-<>?"
file="fuzzy-dict" 


opcion=input("Opcion --> ")
if opcion=="1":
    s=input("Ingrese --> ")
    file=input("Nombre --> ")
elif opcion=="2":
    s=numStri
    print("[0-9]")
elif opcion=="3":
    s=letStriA
    print("[a-z]")
elif opcion=="4":
    s=letStriB
    print("[A-Z]")
else:
    s=letStriA+letStriB+letSymbo+numStri
    print("[a-z]+[A-Z]+[0-9]+[%^&]")

with open(file,'w') as f:
    for n in s:
        f.write(''.join(random.sample(s,len(s)))+'\n')
    f.close()

