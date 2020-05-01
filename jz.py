#!/usr/bin/python3
# -*- coding: utf-8 -*-

import lib.Product as p
import lib.Productlist as l

einkaufsliste = l.Productlist(p)
einkaufsliste.read_csv_file('/home/tn/bin/einkaufliste.csv', ',')
while 1:
    name = input('Geben Sie den Produktnamen an: ')
    preis = input('Geben Sie den Preis an: ')
    gewicht = input('Geben Sie das Gewicht an: ')
    anzahl = input('Geben Sie eine Menge an: ')
    product = p.Product({'Name': name, 'Preis': preis, 'Gewicht': gewicht, 'Anzahl': anzahl})
    einkaufsliste.add_product(product)
    neu = input('Soll ein weiteres Produkt hinzugefuegt werden? (j|n) ')
    if neu != 'j':
        break


einkaufsliste.list_products()
file = '/home/tn/bin/neue_einkaufsliste.csv'
einkaufsliste.write_csv_file(file, ',')


