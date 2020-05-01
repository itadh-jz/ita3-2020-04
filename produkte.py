#!/usr/bin/python3
# -*- coding: utf-8 -*-



# Klasse: Produkt
# Klasseneigenschaft: kategorie
# Objekteigenschaft: Name, Preis(Einheit)
# schreiben Sie eine Methode für je eine Eigenschaft die die Objekteigenschaft setzt
# schreiben Sie eine Methode für je eine Eigenschaft die die Objekteigenschaft holt
# schreiben Sie eine Methode für je eine Eigenschaft die die Objekteigenschaft anzeigt

class Produkt():
    kategorie = 'Nahrungsmittel'

    def set_name(self, name):
        self.name = name

    def set_preis(self, preis):
        self.preis = preis

    def get_name(self):
        return self.name

    def get_preis(self):
        return self.preis

    def show_name(self):
        print(f'Der Name lautet {self.name}')

    def show_preis(self):
        print(f'Der ist {self.preis}')

apfel = Produkt()
apfel.set_name('Apfel')
apfel.set_preis('1')

gurke = Produkt()
gurke.set_name('Gurke')
gurke.set_preis('2')

produkt1 = apfel.get_name()

print('-------')
print(Produkt.kategorie)
print(apfel.kategorie)
print(produkt1)
gurke.kategorie = 'Gemuese'
print(gurke.kategorie)
print(apfel.kategorie)
print(Produkt.kategorie)

print(apfel)

