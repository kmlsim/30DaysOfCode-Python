#!/usr/bin/env python
# -*- coding: utf-8 -*-

testCase = int(raw_input())


if (testCase >= 1 and testCase <= 10):
    loop = 0
    
  
    while (loop < testCase):

        # informa uma string para ser testada.
        string = (raw_input())

        # verifica se a string obedece uma das constraints
        strSize = len(string)
        if ( strSize >= 2 and strSize <= 10000):
            
            even = []
            odd = []
            for i in range(0, strSize):
               if (i % 2 == 0):
                   char = string[i]
                   even.append(char)
               else:
	          char = string[i]
                  odd.append(char)

            print ''.join(even) + " " + ''.join(odd)
        else:
            print "String lenght out of size."
    
        loop = loop + 1

else:
    print "Number of test cases is out of range."

