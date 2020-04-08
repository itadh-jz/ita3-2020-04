#!/usr/bin/python3

def ipaddresse(Addresse):
    ipliste = []
    firstline = True
    with open(Addresse, 'r') as fh:
        for line in fh.readlines():
            if firstline is True:
                firstline = False
                continue

