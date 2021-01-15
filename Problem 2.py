#!/usr/bin/env python
# coding: utf-8

def Fibonacci(n): 
    if n<=1: 
        return (n)
    else: 
        return (Fibonacci(n-1)+Fibonacci(n-2))
  

  
n = int(input()) 
if n > 19 or n<2:
    print("Not in range")
else:
    for i in range(0, n):
        list=(Fibonacci(i))
        print(list, end = ", ")     #Problem is: At the end of output, it shows comma. 0, 1, 1, 2, 3, 5, 8, 13,





