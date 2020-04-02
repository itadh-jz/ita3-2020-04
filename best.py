#!/usr/bin/python3                                                                   


obst = ['Apfel', 'Banane', 'Birne', 'Kiwi']

for frucht in obst:
    eingangsfrage = input('Soll etwas ausgegeben werden?')
    if eingangsfrage == 'J' or eingangsfrage == 'j':
        print(frucht)

frage = input('Soll die Frucht ausgegeben werden? [J|N]: ')
#    if frage == 'J':
#        print(frucht)
#    elif frage == 'j':
#        print(frucht)

    if frage == 'j' or frage == 'J' or frage == 'y' or frage == 'Y':
        print(frucht)

