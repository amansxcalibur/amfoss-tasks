#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum=0
    n1=1
    n2=1
    n3=0
    while n2<n:
        if n2%2==0:
            sum+=n2
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    print(sum)