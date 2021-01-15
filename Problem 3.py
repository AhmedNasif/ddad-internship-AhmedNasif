#!/usr/bin/env python
# coding: utf-8

def my_function(x):
  return x[::-1]


print("Enter a string")
n = input()
revText = my_function(n)
if n.lower() == revText.lower():
    if (len(n)%2==0):
        print("Even Palindrome")
    else:
        print("Odd Palindrome")
else:
    print("Not a Palindrome")

