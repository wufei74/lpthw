# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 16:41:44 2020

@author: WufeiNewPC
"""


#ex14

from sys import argv

script, user_name, password = argv
prompt = '==> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me{user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice one, {user_name}.
Also, your password is {password}. Don't put that in plain text
""")


      
