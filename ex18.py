# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 19:24:57 2020

@author: WufeiNewPC
"""


#ex18.py

# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2, arg3 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
    print(args)
        
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")
    print(arg1)
    
#@this one takes no arguments
def print_none():
    print("I got nothin.'.", flush=True)
    
print_two("Zed", "Shaw", "fdasfsda")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

        