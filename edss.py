# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 10:06:05 2017

@author: harne
"""

def numberOf(theList, v):
    count = 0
    if(theList[0]==v):
        print(theList)
        return 1
    else:
        return count + numberOf(theList[1:], v)
    
    return count
    
print(numberOf([4, 5, 6, 6, 7], 6))