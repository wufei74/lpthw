#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 21:06:54 2020

@author: wufei
"""

print("Whats the name of your file you want to read?")
filename = input("? >")


target = open(filename)

print(target.read())

print(f"Closing file {filename}.")
target.close()
