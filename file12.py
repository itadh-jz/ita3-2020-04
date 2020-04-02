#!/usr/bin/python3


obst = ['Apfel', 'Banane', 'Birne', 'Kiwi']

#eingangsfrage = input('Soll ueberhauptnichts etwas ausgegeben werden? [J|N]: ')

for frucht in obst:
#    if eingangsfrage == 'j' or eingangsfrage == 'J' or eingangsfrage == 'y' or eingangsfrage == 'Y':
##        break
#        continue

#################################
    if frucht == 'Birne':
        continue
#################################

    frage = input('Soll die Frucht ausgegeben werden? [J|N]: ')
#    if frage == 'J':
#        print(frucht)
#    elif frage == 'j':
#        print(frucht)

    if frage == 'j' or frage == 'J' or frage == 'y' or frage == 'Y':
        print(frucht)

print('uff, geschafft') 
