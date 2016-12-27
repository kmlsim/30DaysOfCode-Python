#!/bin/python
# -*- coding: utf-8 -*-

import math

remain = 0
consecutives = 0
max_consecutives = 0

n = int(raw_input())

if (n >= 1 and n <= pow(10,6)):
    while (n > 0):
        remain = n % 2
        n = n / 2
        if remain == 1:
            consecutives += 1
            if consecutives >= max_consecutives:
                max_consecutives = consecutives
        else:
            consecutives = 0
print max_consecutives
