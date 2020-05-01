#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import os
import lib.Product as p
import lib.Productlist as l

# schreiben Sie eine Abfrage die die zu verarbeitende Datei abfragt.
# Dabei soll das Suffix .csv für CSV Dateien stehen und das Suffix .json für JSON Dateien.
# schreiben Sie eine Abfrage als was die aktuellen Daten gespeichert werden sollen. z.B JSON oder CSV.

einkaufsliste = l.Productlist(p)
os.system('clear')

######### 1. Aufgabe ############
#einkaufsliste.read_csv_file('/home/tn/bin/einkaufliste.csv', ',')
#einkaufsliste.write_csv_file('/home/tn/bin/einkaufliste-1.csv', ';')

input_file = input('Geben Sie die Datei an die eingelesen werden soll: ')
if input_file[-3:] == 'csv':
    delimiter = input('Geben Sie das Trennzeichen der CSV Datei ein: ')
    print(delimiter)
    einkaufsliste.read_csv_file(input_file, delimiter)
elif input_file[-4:] == 'json':
    einkaufsliste.read_json_file(input_file)
else:
    print('Die Datei hat kein gültiges Suffix!')
    exit(1)
#################################


while 1:
#    os.system('clear')
    print( 50 * '-')
    print('Wählen Sie eine Zahl für eine Aktion aus')
    print('1 - neues Produkt anlegen')
    print('2 - bestehende Daten in eine CSV Datei schreiben')
    print('3 - bestehende Daten in eine JSON Datei schreiben')
    print('4 - alle Produkte auflisten')
    print('5 - Program beenden')
    cmd = input('Wählen Sie eine Zahl für eine Aktion aus: ')
    if cmd == '1':
        name = input('Geben Sie den Produktnamen an: ')
        preis = input('Geben Sie den Preis an: ')
        gewicht = input('Geben Sie das Gewicht an: ')
        anzahl = input('Geben Sie eine Menge an: ')
        product = p.Product({'Name': name, 'Preis': preis, 'Gewicht': gewicht, 'Anzahl': anzahl})
        einkaufsliste.add_product(product)
    elif cmd == '2':
        out_file = input('Geben Sie den Dateinamen an in die die Daten geschrieben werden sollen: ')
        delimiter = input('Geben Sie das Trennzeichen an: ')
        einkaufsliste.write_csv_file(out_file, delimiter)
    elif cmd == '3':
        out_file = input('Geben Sie den Dateinamen an in die die Daten geschrieben werden sollen: ')
        einkaufsliste.write_json_file(out_file)
    elif cmd == '4':
        einkaufsliste.list_products()
        input('weiter')
    elif cmd == '5':
        exit(0)
    else:
        print('Ihre Eingabe war ungültig')
        time.sleep(10)
#        exit(2)


######### 2. Aufgabe ############
#einkaufsliste.write_csv_file('/home/tn/bin/einkaufliste-1.csv', ';')
#einkaufsliste.write_json_file('/home/tn/bin/einkaufliste.json')
#################################


