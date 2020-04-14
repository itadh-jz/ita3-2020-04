#!/usr/bin/python3
# -*- coding: utf-8 -*-

def is_something(pattern, liste):
    for item in pattern:
        schalter = False
        for element in liste:
            print(f'vergleiche {item} mit {element}')
            if item == element:
                schalter = True
                break
        if schalter is False:
            return False
    return True


#############################
liste = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
while 1:
    eingabe = input('Geben Sie die zu pruefende Zeichenkette ein: ')
    result = is_something(eingabe, liste)
    print(result)
#    result = True
#    for item in eingabe:
#        if item not in liste:
#            result = False
#    print(result)



