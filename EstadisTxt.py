#!/usr/bin/env python
#-*-coding: utf-8 -*-

import os
# from tabulate import tabulate


def count_char(txt,char):
    count=0
    for c in txt:
        if c == char:
            count += 1
    return count

os.system('clear')
f=input(" --> ")
lineas= 0

with open(f, 'r') as file:
    for line in file:
        if line != "\n":
            lineas += 1


with open(f, 'r') as file:
    data = file.read().replace('\n', '')
    file.close()

text=data
largo=len(text)
os.system('clear')
print(f"\n=================================")
print(f"Total de Lineas: {lineas}")
print(f"Total de Caracteres: {largo}")
print(f"Char/Linea(Aprox.): ",round(largo/lineas,2))
print(f"=================================\n")
print(f"Char\tPorc.\tTotal\tAp/Li")

for char in "abcdefghijklmnñopqrstuvwxyz":
    percent = 100 * count_char(text,char)/ len(text)
    total=count_char(text,char)
    if total==0:
        divi="*****"
    else:
        divi=round(1/(lineas/total),2)

    
    print("{0} ->\t{1}%\t{2}\t{3}".format(char,round(percent,2),total,divi))

print(f"\n================================\n")

