#Section 1: Terminology
# 1) What is a recursive function?
# A recursive function is a function that calls itself.
#
#
# 2) What happens if there is no base case defined in a recursive function?
# The program would keep recursing itself. 
#
#
# 3) What is the first thing to consider when designing a recursive function?
# What the base case is
#
#
# 4) How do we put data into a function call?
# Define a function
#
# 
# 5) How do we get data out of a function call?
# Return
#
#

#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables q1-q20.

#a1 = 8
#a2 = 8
#a3 = -1

#b1 = 2
#b2 = 2
#b3 = 4

#c1 = 3
#c2 = 4
#c3 = 5

#d1 = 6
#d2 = 8
#d3 = 4

#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.

import random
import math

def check(number,avg):
	if int(number) == 1 or int + 2:
		avg += int(number)
		user(avg)

def user(avg):
	number = raw_input("Next number:")
#this is base case
	if number == "":
		check(number,avg)
		print "The average of your odd numbers are {}".format(avg)
#this is recursive case
	else:
		check(number,avg)
		user(avg)

def main():
	avg = 0
	user(avg)
main()





