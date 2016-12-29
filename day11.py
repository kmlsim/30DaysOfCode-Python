# -*- coding: utf-8 -*-
#!/bin/python

n = 6
arr = []
x = 0
maxHourglass = 0
greater = 0
lista = []

for arr_i in xrange(n):
   arr_temp = map(int,raw_input().strip().split(' '))
   arr.append(arr_temp)

for i in range(n):
    for j in range(n):
        if ((arr[i][j]) >= -9 and (arr[i][j]) <= 9):
            while ( x < n-2):
                y = 0
                while (y < n-2):
                    sumHourglass = ((arr[0+x][0+y]) + (arr[0+x][1+y]) + (arr[0+x][2+y])  + (arr[1+x][1+y]) \
                    + (arr[2+x][0+y]) + (arr[2+x][1+y]) + (arr[2+x][2+y]))
                    y += 1
                    lista.append(sumHourglass)
                x += 1
        else:
            print "Element A%d,%d it's out of range" % (i, j)
print max(lista)
