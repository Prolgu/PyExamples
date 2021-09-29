#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dado.py
#  
#  



import random

def dado(a=0,b=0):
    c=random.randrange(a,b)
    print(c)
    return 0

quest=input("Seleccione el tipo de dado:\n1 - d6\n2 - d20\n3 - d100\n>>> ")


if quest=="1":
    dado(1,6)
elif quest=="2":
    dado(1,20)
elif quest=="3":
    dado(1,100)
else:
    print("Error")

