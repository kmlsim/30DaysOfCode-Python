#!/bin/python

import sys


S = raw_input().strip()
try:
    output = int(S)
    print output
except ValueError:
    print 'Bad String'
