 4# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 19:52:57 2020

@author: WufeiNewPC
"""


#ex19

#Create the function c_a_c so we can call it later
#it takes two arguements, c_c and b_o_c.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!") #Print c_C
    print(f"You have {boxes_of_crackers} boxes of crackers!") #print b_o_c
    print("Man that's enough for a party!")
    print("Get a blanket. \n")

#Call our function with two arguements, 20, 30.     
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

#Set two variables in the script a_o_c and a_o_cr.
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

#Call our function again using our variables we set.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


#Call our function. We can do math now inside of it for the arguments
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

#Call our function once more. Now we use variables + arguments via math.
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 10)


#Create our own function that calculates covid deaths per player
#in baseball. 
def baseball_players(player_count, covid_deaths_us):
    print("Covid has seriously ruined this country.\nIt's time for change.")
    print(f"There are {player_count} baseball players currently.")
    print(f"There are {covid_deaths_us} Covid deaths in the US.\n")
    #Create variable to calculate deaths per player
    #Convert the input from the user to numbers using int()
    death_per_player = int(covid_deaths_us) / int(player_count)
    #print the number of deaths per player
    print(death_per_player)
    print("\n That's how many deaths there are per player.")
    
#Ask for input from user. Store those responses as variables
user_player_count = input("How many baseball players are there? ")
user_covid_count = input("How many Covid deaths are there in the US? ")

#Call our function using the input from the users as the arguments
baseball_players(user_player_count, user_covid_count)
