#!/bin/python

import sys


n = int(raw_input().strip())

while n >= 2 and n <= 20:
    for i in range(10):
        print "%d x %d = %d" % (n, i + 1, n * (i + 1))
    break
