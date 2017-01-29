#!/bin/python

import sys


n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))

numOfSwaps = 0

for i in range(len(a)-1, 0, -1):
    for j in range(i):
        if (a[j] > a[j+1]):
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            numOfSwaps += 1

print a
print "Array is sorted in %d swaps." % numOfSwaps
print "First Element: %d" % a[0]
print "Last Element: %d" % a[n-1]
