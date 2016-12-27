#!/bin/python
# -*- coding: utf-8 -*-
#import pdb; pdb.set_trace()

n = int(raw_input())

if (n >= 2 and n <= 12):
    def factorial(n):
        if (n == 1):
            return 1
        else:
            return n * factorial(n-1)
else:
    print "Fora da escala."

print (factorial(n))
