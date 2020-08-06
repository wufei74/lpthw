# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 16:51:40 2020

@author: WufeiNewPC
"""


#ex15

#Import argv so we can use arguments
from sys import argv

#Create two variables, script and filename. Script is always the first thing pulled from argv, the second is the filename provided by the user
script, filename = argv

#Create variable, txt. We then open the filename provided by the user via argument.
#This lets us access said file
txt = open(filename)

#Print the name of this script
print(f"Here's our script {script}")

#Print the filename the user provided via arg
print(f"Here's your file {filename}:")

#Now we call the .read function on the filename provided
#Then we print it directly to the terminal
print(txt.read())

#Close the file object that we had open and print that we did
txt.close()
print(f"closed file {filename}")


#Print again a request for the filename to the user
print("Type the filename again:")

#Create variable file_again, and get the input from the user with a prompt >
file_again = input("> ")

#Now we create a variable to hold our file being opened.
txt_again = open(file_again)

#Call the .read function on our second file name request, and then print it to terminal
print(txt_again.read())

#Close once again the file
txt_again.close()
print(f"We closed the file {file_again}")

