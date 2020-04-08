#!/usr/bin/python3
# -*- coding: utf-8 -*-

file = '/home/tn/bin/network_stuff.csv'

first_line = True
with open(file, 'r') as fh:
    for line in fh.readlines():
        if first_line is True:
            first_line = False
            continue
        rows = line.split(';')
        pattern = rows[0]
        octett = pattern.split('.')

        len = 0
        for i in octett:
            len = len + 1

        if len == 4:
            print(f'Treffer ok: {octett}')
        else:
            print(pattern)
            print('WEG DAMIT')
