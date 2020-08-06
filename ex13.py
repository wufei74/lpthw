# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 15:54:28 2020

@author: WufeiNewPC
"""


#ex13.py

from sys import argv
# Ready the WYSS section for how to run this
script = argv

print("The script is called:", script)
first = input("Try typing a word")
print("Your first variable is:", first)

second = input("Lets do a second word")
print("Your second variable is:", second)

third = input("Lets try again")
print("Your third variable is:", third)

print("\n", script, first, second, third, sep="--")