# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 22:12:41 2017

@author: harne
"""

def caesarCipher(word, shift):
    new_word = ''
    start = 0
    for char in word:
        if char.isupper():
            start = ord('A')
        elif char.islower():
            start = ord('a')
        new_word += chr((ord(char)-start+shift)%26 + start)
    return new_word

print(caesarCipher('IBM', -1))