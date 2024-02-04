#!/bin/python3

import sys

t=int(input())
for x in range (t):
    n = int(input())
    found = False
    f=1
    for i in range(1,n+1):
        f=f*i

    for number in range(n, f+1):
        d = True
        for i in range(1, n+1):
            if number % i != 0:
                d = False
                break
        if d:
            found = True
            print(number)
            break