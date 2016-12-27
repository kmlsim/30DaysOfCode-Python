#!/bin/python
# -*- coding: utf-8 -*-

import math

my_dict = {}
lista = []
    n = int(raw_input())

if (n >= 1 and n <= math.pow(10,5)):
    for i in range(n):
        info = raw_input().split()
        lista.append(info)
        my_dict = {name: phoneNumber for name, phoneNumber in lista}

    print my_dict

    for i in range(100000):
        searchName = raw_input()
        if searchName in my_dict:
            print "%s=%s" % (searchName, my_dict[searchName])
        else:
            print "Not found"
    else:
        print "não pode"
else:
    print "Number out of range."
