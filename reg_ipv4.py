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
        octetts = pattern.split('.')

        l = 0
        for i in octetts:
            l = l + 1
 
        if l != 4:
            continue

##################################
        items = octetts[3].split('/')
        l = 0
        for i in items:
            l = l + 1

        # 
        if l == 1:
            # keine Netmask
            print('no netmask')
        elif l == 2:
            # habe Netmask
            print('netmask')
        else:
            continue

        print(octetts)
        

        

#            print(f'Treffer ok: {octetts}')
#            for octett in octetts:
#                for zeichen in octett:
#                    print(zeichen)
#
