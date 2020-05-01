#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Produkt():

    #produkt0 = {'Name': 'Milch',
    #           'Preis': 1,
    #           'Gewicht': 1000,
    #           'Anzahl': 4}
    def __init__(self, eigenschaft):
    #def __init__(self):
        print('Ich bin erschaffen worden')
        self.attribut = eigenschaft
 
    def set_attribut(self, kiey, value):
#        self.attribut = {}
        self.attribut[kiey] = value

    def get_attribut(self):
        return self.attribut

#Apfel = Produkt()
#Apfel.set_attribut('Name', 'Apfel')
#Apfel.set_attribut('Farbe', 'gruen')
#Birne = Produkt()

apfel = Produkt({'Name': 'Apfel', 'Farbe': 'gruen'})


#print(apfel.get_attribut())
##apfel.set_attribut('Name', 'Apfel')
#apfel.set_attribut('Farbe', 'gruen')

print(apfel.get_attribut())

