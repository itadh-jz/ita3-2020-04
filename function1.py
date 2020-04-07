#!/usr/bin/python3

int0 = 50
debug = True
def berechnung(int1, int2, int3):
    if debug is True:
        print(int0)
    result = int1 * int2 + int3
    return result

print('-' * 50)
print('da passiert etwas')
debug = False
ergebnis = berechnung(2,3,4)
print('da passiert noch etwas')
print('da passiert noch mehr')
print(ergebnis)













#name = 'Jörg Zimmermann'
#print ( name[0] ) 
#
#print ( name.upper() )

