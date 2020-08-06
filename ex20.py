#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 18:14:25 2020

@author: wufei
"""

#ex20.py
#import modules for arguments
from sys import argv
#Set arguments to variables
script, input_file=argv

#Create function for printing an entire open file
def print_all(f):
    print(f.read())
    
#Go back to the start of file f
def rewind(f):
    f.seek(0)
    
#Create function that requires 2 variables. Line_count, 
#which shows which line we're on currently.
#and F, which is the file we want to read the line from.
#Readline reads one line at a time.    
def print_a_line(line_count, f):
    print(line_count, f.readline())
    
#Set variable for open file for our argument given filename.
    #so we can access it.
current_file = open(input_file)


print("First, let's print the whole file:\n")

# callour function p_a that reads an open file and prints it
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

#Since the file is open and it reads one at a time, we need to go
#back to the beginning of the file so we can do it one line
#at a time.
rewind(current_file)


print("Let's print three lines:")

#This sets the current counter of line to 1. We are at the 
#0 byte of our open file. Now it will read one line at 
#a time, and we then add one to the current_line count

current_line = 1
print_a_line(current_line, current_file)
print(current_line)
current_line += 1
print_a_line(current_line, current_file)
print(current_line)
current_line += 1
print_a_line(current_line, current_file)
print(current_line)
print("Closing file ", current_file.name)
current_file.close()

#Testing this to verify that readline will keep going and 
#remember where it was. It does. We just use the current_line
#as a viewable count for the user.
#rewind(current_file)
#print(current_file.readline())
#print(current_file.readline())
#print(current_file.readline())
#print(current_file.readline())
#print(current_file.readline())
#print(current_file.readline())
#print(current_file.readline())