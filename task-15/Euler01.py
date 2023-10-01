#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum=0
    for i in range(n-1,0,-1):
        if i%3==0:
            sum+=(i/3)*(3+i)/2
            break
    for i in range(n-1,0,-1):
        if i%5==0:
            sum+=(i/5)*(5+i)/2
            break
    for i in range(n-1,0,-1):
        if i%15==0:
            sum-=(i/15)*(15+i)/2
            break
    print(int(sum))
