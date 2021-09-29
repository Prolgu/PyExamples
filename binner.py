#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  binner.py
#
#
#
entry=int(input("Ingrese numero --> "))

print("Valor en Binario: ",bin(entry))
print("Valor en Hexadecimal: ",hex(entry))

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
