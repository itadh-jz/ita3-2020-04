#!/usr/bin/python3

# Dictionary
person = {'first': 'Perter', 'last': 'Schmidt'}
print(person['first'])

# Liste
obst = ['apfel', 'birne', 'kiwi']
print(obst[0])

# Tupel
obst = ('apfel', 'birne', 'kiwi')
print(obst[0])

#teilnehmer = [ {'first': 'Erna', 'last': 'Mayer'}, {'first': 'Fred', 'last': 'Tischler'}, {'first': 'Karsten', 'last': 'Schmidt'}]

# Teilnehmer
# Erna, Mayer
# Fred, Tischler
# Karsten, Schmidt

person_a = {'first': 'Erna', 'last': 'Mayer'}
person_b = {'first': 'Fred', 'last': 'Tischler'}
person_c = {'first': 'Karsten', 'last': 'Schmidt'}

#print(teilnehmer[1]['last'])
print(person_b['last'])
teilnehmer = [person_a, person_b, person_c]
print(teilnehmer[0]['first'])

