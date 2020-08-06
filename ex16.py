#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 20:52:29 2020

@author: wufei
"""

#ex16

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

#print("Truncating the file. Goodbye!")
#target.truncate()

input("QUit now")
print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

#Using the escape character\n, i was able to print all three lines spaced out in one line of code!
target.write(f"{line1}\n{line2}\n{line3}")

print("And finally, we close it.")
target.close()
