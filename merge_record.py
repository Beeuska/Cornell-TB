# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 15:31:38 2017

@author: harne
"""

def merge_records(d1, d2):
    for key in d2.keys():
        if key not in d1.keys():
            d1[key]= d2[key]
        else:
            for i in range(len(d2[key])-1):
                d1[key][i]+= d2[key][i]

d1 = {"Cornell": [10, 1], "Harvard": [4, 3]}
d2 = {"Cornell": [2, 0], "Stanford": [0, 3]}

merge_records(d1, d2)
print (d1)