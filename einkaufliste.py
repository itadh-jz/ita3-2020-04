#!/usr/bin/python3

name = 'Peter Lustig'
alter = 32
person = name
groesse = '180'
name = 'Fred Feuerstein'

einkaufsliste = [ 'Mich', 'Butter', 'Eier', 'Brot', 'Saft', 'Honig', 'Käse', 'Wurst' ]
preise = [ 1, 1, 3, 3, 4, 2, 2, 4 ]
anzahl = [ 2, 3, 1, 1, 1, 2, 3, 4, 3, 5, 6, 7]



produkt0 = {'Name': 'Milch',
           'Preis': 1,
           'Anzahl': 4}

produkt1 = {'Name': 'Butter',
           'Preis': 1,
           'Anzahl': 2}

produkt2 = {'Name': 'Eier',
           'Preis': 3,
           'Anzahl': 1}

einkaufsliste = [ produkt0, produkt1, produkt2 ]



zaehler = 0
kosten = 0
for nahrungsmittel in einkaufsliste:

    produktkosten =  anzahl[zaehler] * preise[zaehler]
    kosten = kosten + produktkosten
    zaehler = zaehler + 1 

    
#    if kosten > 10:
#        break
#    print(zaehler)
#    print(kosten)
#    print(nahrungsmittel)
#    a = input()
    if kosten < 11:
        print(zaehler)
        print(kosten)
        print(nahrungsmittel)
    a = input()

print('Ende')






















#print(name[0:5])
#print(name[6:])
#print(name[2:5])


