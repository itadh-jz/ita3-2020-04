#!/usr/bin/python3
# -*- coding: utf-8 -*-


file = '/home/tn/bin/network_stuff.csv'

# Funktion die prueft ob alle Zeichen der Eingabe in einer gegebenen Liste enthalten sind
# Die Funktion gibt True odder False zurueck
def is_something(pattern, liste):
    for item in pattern:
        schalter = False
        for element in liste:
            if item == element:
                schalter = True
                break
        if schalter is False:
            return False
    return True

# Datei einlesen und die erste Zeile ueberspringen
first_line = True
with open(file, 'r') as fh:
    for line in fh.readlines():
        # erste Zeile ueberspringen
        if first_line is True:
            first_line = False
            continue
        # die erste Spalte ermitteln
        rows = line.split(';')
        # die erste Spalte in Oktetts zerlegen und in einer Liste speichern
        pattern = rows[0]
        octetts = pattern.split('.')

        # ermittelen der Lange der Liste
        l = 0
        for i in octetts:
            l = l + 1
 
        # es kann nur eine IP Adresse sein wenn es genau vier Oktetts gibt
        if l != 4:
            continue

        # Das letzte Oktett kann eine Netzmaske enthalten
        items = octetts[3].split('/')
        l = 0
        for i in items:
            l = l + 1

        # Wenn die Lange des letzten Oktetts 1 ist, haben wir keine Netzmaske
        if l == 1:
            netmask = ''
        # Wenn die Lange des letzten Oktetts 2 ist, haben wir eine Netzmaske
        elif l == 2:
            octetts[3] = items[0]
            netmask = items[1]
        else:
            continue

        # enhaelt ein Oktett ungueltige Zeichen
        # (gueltige Zeichen sind die Zahlen 0 bis 9)
        invalid = False
        liste = ['0','1','2','3','4','5','6','7','8','9']
        for octett in octetts:
            result = is_something(octett, liste)
            # Wenn die enthaltenen Zeichen nur Zahlen sind pruefen wir ob das Oktett 
            # zwischen 0 und 256 liegt
            if result is not False:
                _octett = int(octett)
                if _octett >= 0 and _octett <= 255:
                    pass
            else:
                # Das Oktett liegt ausserhalb des gueltigen Bereichs
                invalid = True
                break
        if invalid is True:
            break

        # Wenn es eine Netzmaske gibt pruefen wir ob sie gueltig ist (2 bis 30)
        if netmask != '':
            invalid = False
            liste = ['0','1','2','3','4','5','6','7','8','9']
            result = is_something(netmask, liste)
            if result is not False:
                _netmask = int(netmask)
                if _netmask >= 2 and _netmask <= 30:
                    pass
                else:
                    invalid = True
            if invalid is True:
                break

        # Ergebnis
        print(f'IP: {octetts[0]}.{octetts[1]}.{octetts[2]}.{octetts[3]} -- Netmaske: {netmask}')

