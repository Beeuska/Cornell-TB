# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 14:03:47 2017

@author: harne
"""

def putSideBySide(two_line_strings):
    start_string = ''
    end_string = ''
    for i in range(len(two_line_strings)):
        start_string += two_line_strings[i][0:2] + " "
        end_string += two_line_strings[i][3:] + " "
    return start_string + "\n" + end_string

print (putSideBySide(["AB\nCD", "EF\nGH", "IJ\nKL"]))

print (len("AB\nCD"))