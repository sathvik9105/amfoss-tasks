#!/bin/python3

import sys

def palindrome(s):
    return s == s[::-1] 
    
def largest(n):
    answer = 0
    for i in range(999,99,-1):
        for j in range(i,99,-1):
            p=i*j
            if p<n and palindrome(str(p)) and p>answer:
                answer = p
            elif p < answer:
                break
    return answer

t = int(input().strip())
for x in range(t):
    n = int(input().strip())
    y = largest(n)
    print(y)