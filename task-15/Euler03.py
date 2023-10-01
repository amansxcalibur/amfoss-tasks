#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    for i in range(n,0,-1):
        count=0
        if n%i==0:
            for j in range(2,i):
                if i%j==0:
                    count+=1
            if count==0:
                print(i)
                break