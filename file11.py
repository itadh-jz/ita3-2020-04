#!/usr/bin/python3


obst = ['Apfel', 'Banane', 'Birne', 'Kiwi']

eingangsfrage = input('Soll ueberhaupt etwas ausgegeben werden? [J|N]: ')

if eingangsfrage == 'j' or eingangsfrage == 'J' or eingangsfrage == 'y' or eingangsfrage == 'Y':
    for frucht in obst:
        frage = input('Soll die Frucht ausgegeben werden? [J|N]: ')
    #    if frage == 'J':
    #        print(frucht)
    #    elif frage == 'j':
    #        print(frucht)
    
        if frage == 'j' or frage == 'J' or frage == 'y' or frage == 'Y':
            print(frucht)

        
