# -*- coding: utf-8 -*-
#!/bin/python

# table= [ [ 0 for i in range(5) ] for j in range(5):  ]

#[[row[i] for row in matrix] for i in range(4)]
n = 2
arr = []

for arr_i in xrange(n):
   arr_temp = map(int,raw_input().strip().split(' '))
   arr.append(arr_temp)

for i in range(n):
    for j in range(n):
        if ((arr[i][j]) > 9):
            print "Element A%d,%d it's out of range" % (i, j)
        else:
            for i in range(n):
