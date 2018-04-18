# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 22:22:46 2017

@author: harne
"""

#CS 2110 Practice

#Question 1

def Fact(N):
    if N == 1:
        return 1
    else:
        return N*Fact(N-1)
    
#Question 2

def CompNat(N):
    if N==1:
        return 1
    else:
        return N+CompNat(N-1)

#Question 3

def multiply(a, b):
    if(b==1):
        return a
    else:
        return a+multiply(a, b-1)

print(multiply(10, 4))

#Question 4

def GCD(x, y):
    if x%y == 0:
        return y
    else:
        return GCD(x, x%y)


print(GCD(96, 64))

#Question 5

def root(x, n):
    if(n==1):
        return x
    else:
        return '1/' +str(x*root(x, n-1))
print(root(8, 2))

#Question 6

    