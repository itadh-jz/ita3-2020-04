#!/usr/bin/python3

types = { 'name': 'string', 'preis': 'int', 'gewicht': 'int', 'anzahl': 'int' }

def get_value(typen, attribute, value):
    if typen[attribute] == 'string':
        value = value[1:]
        value = value[:-1]
        return value
    if typen[attribute] == 'int':
        return int(value)


def datei_einlesen(Datei):
    _einkaufsliste = []
    firstline = True
    # einlesen der Daten aus einer CSV Datei
    with open(Datei, 'r') as fh:
        for line in fh.readlines():
            if firstline is True:
                firstline = False
                continue
            items = line.split(',')

            name = get_value(types, 'name', items[0])
            preis = get_value(types, 'preis', items[1])
            gewicht = get_value(types, 'gewicht', items[2])
            anzahl = get_value(types, 'anzahl', items[3])

#            name = items[0][1:]
#            name = name[:-1]
#            preis = int(items[1])
#            gewicht = int(items[2])
#            anzahl = items[3]
#            anzahl = int(anzahl[:-1])

            nahrungsmittel = {'Name': name, 'Preis': preis, 'Gewicht': gewicht, 'Anzahl': anzahl}
            _einkaufsliste.append(nahrungsmittel)
    return _einkaufsliste

einkaufsliste = datei_einlesen('/home/tn/bin/ekliste.csv')


