# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 13:54:00 2020

@author: WufeiNewPC
"""


types_of_people = 10 #Variable 
x = f"There are {types_of_people} types of people." #x is a string that includes our previous variable, also a string

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}." #y is another formatted{hence the f in front} string which has two strings included in it, from two variables 

print(x) #This prints the x string, which includes our variable "types_of_people"
print(y) #This prints the y string, which includes the variables "binary" and "do_not"

print(f"I said: {x}") #Another formatted string which includes the x variable, which calls the types_of_people variable
print(f"I also said: '{y}'") #Another formatted string that calls on and prints the variable string "y" in quotes.

hilarious = False #True/false variable 
joke_evaluation = "Isn't that joke so funny?! {}" #This leaves an empty call for a variable at the end

print(joke_evaluation.format(hilarious)) #This prints the "joke_evaluation" variable string, and also calls to format it and input variable "hilarious" where the {} is.

w = "This is the left side of..."
e = "a string with a right side."

print(w + e) #This + is actually concatenating the string. Notice there are no spaces inbetween w and e when printed.
