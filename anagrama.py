#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  anagrama.py
#  
#  

import random

stri=input("Ingrese su cadena maquinola \n-> ")

def anagrama(s):
    for n in s:
        print(''.join(random.sample(s,len(s))))
    # return 

anagrama(stri)
