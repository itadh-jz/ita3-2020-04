#!/usr/bin/python3


teilnehmer = [ 
    {'first': 'Erna', 'last': 'Mayer'}, 
    {'first': 'Fred', 'last': 'Tischler'}, 
    {'first': 'Karsten', 'last': 'Schmidt'}]

zaehler = 0
for teil in teilnehmer:
    zaehler = zaehler + 1
    print(zaehler)

    var = 'last'
    print(teil[var])
    print('-'*10)

