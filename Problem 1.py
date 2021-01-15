#!/usr/bin/env python
# coding: utf-8

n = int(input()) 
if n > 9 or n<1:
    print("Not in range")

else:
    fac = 1
    for i in range(1,n + 1):
        fac = fac*i
    print(fac)

