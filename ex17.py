#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 20:09:38 2020

@author: wufei
"""

#ex17

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

indata = open(from_file).read()


print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w'); out_file.write(indata)

print("Alright, all done.")

out_file.close()
