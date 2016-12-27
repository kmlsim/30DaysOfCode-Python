#!/bin/python
# -*- coding: utf-8 -*-
import pdb
import sys


n = int(raw_input().strip())
listArray = []

if (n >= 1 and n <= 1000):
    arr = map(int,raw_input().strip().split(' '))

    if (len(arr) == n):
        for i in reversed(range(n)):
            elem = arr[i]
            listArray.append(elem)
        print ' '.join(map(str, listArray))
    else:
        print "Numbers of elements differents!"
else:
    print "Size of array is out of range."
