# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 16:00:59 2017

@author: harne
"""

def swap(b, h, k):
    b[h], b[k] = b[k], b[h]

def string_list_sort(b,h,k):
    i = h -1
    t = k+1
    while i<t-1:
        if type(b[i])==str:
            i += 1
        else:
            swap(b, i+1, t-1)
            t-=1

b = [["fuck"], "how", ["frick"]]

string_list_sort(b, 0, 2)

print (b)
print (len([]))