#!/bin/python
# -*- coding: utf-8 -*-

import math

my_dict = {}
n = int(raw_input("Informe o número de entradas na agenda telefonica: "))

if (n >= 1 and n <= math.pow(10,5)):
    for i in range(n):
        # name = raw_input("Inform nome: ")
        # phoneNumber = int(raw_input("Informe numero de telefone: "))
        info = map(str, raw_input().strip().split(' '))
        n = 0
        while (n < len(info)):
            print info[n]
            print info[(n+1)]
            # my_dict[info[n]] = info[(n+1)]
            # print my_dict
            n = n+1

        #my_dict[name] = phoneNumber
        print my_dict

    queries = int(raw_input("Informe a quantidade de consultas no dic."))
    if (queries >= 1 and queries <= math.pow(10,5)):
        #size = len(my_dict)
        for indexForQueries in range(queries):
            searchName = raw_input("Procura nome: ")
            if searchName in my_dict:
                print "%s=%s" % (searchName, my_dict[name])
            else:
                print "Not found"

    else:
        print "não pode"

else:
    print "Number out of range."
