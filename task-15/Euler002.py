#!/bin/python3

import sys

t = int(input())
for x in range(t):
    n = int(input())
    a,b,sum = 0,1,0
    for i in range (n):
        if a>=n:
            break
        if a%2==0:
            sum+=a
        a,b = b,a+b
    print(sum)
    