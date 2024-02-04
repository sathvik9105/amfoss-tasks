#!/bin/python3

import sys

def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


t = int(input())
for x in range(t):
    n = int(input())
    largest_prime = largest_prime_factor(n)
    print(largest_prime)