#!/usr/bin/env python
# coding: utf-8

fiboFirstDigit = 0
fiboSecondDigit = 1
n = int(input()) 
if n > 19 or n<2:
    print("Not in range")
else:
    i = 1
    while i <= n:
        if i<n:
            i+=1
            print (fiboFirstDigit,end=", ")
        elif i==n:
            print (fiboFirstDigit)
            break
        nextDigit = fiboFirstDigit + fiboSecondDigit
        fiboFirstDigit = fiboSecondDigit
        fiboSecondDigit = nextDigit

