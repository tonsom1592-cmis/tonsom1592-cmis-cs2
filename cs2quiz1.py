#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for?
#The symbol "=" is used to assign a value. 
#
#
#2 3pts) Write a technical definition for 'function'
#A function is a sequence of instructions to perform a calculation. 
#
#
#3 1pt) What does the keyword "return" do?
#The keyword "return" is used to give the final output of a function, and is used inside a function as a statement.
#
#
#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below
#	1: int = 3,-5
#	2: str = " Hello World " , " How are you? "
#	3: float = 5.5, 5.76
#	4: tuple = (" My "," name "," is "," Tonsom ") , (" I "," am "," 17 "," years "," old ")
#	5: bool = True , False
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
# A function definition is naming a function, and calculating the statements. #Meanwhile, a function call is calling a defined function to perform a #calculation, and present the result to its caller. 
#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them
#	1: Input- The computer receives commands
#	2: Process- Uses the commands and performs a caluculation
#	3: Output- Presents the results of the calculations
#
#Part 2: Programming (25 points)
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:
import math
def radiusOfCircle1(a):
	diameter = (math.sqrt((a/math.pi)))*2
	return diameter

def radiusOfCircle2(b):
	diameter = (math.sqrt((b/math.pi)))*2
	return diameter

def radiusOfCircle3(c):
	diameter = (math.sqrt((c/math.pi)))*2
	return diameter

def main():
	C1 = int(raw_input("Area of C1:"))
	C2 = int(raw_input("Area of C2:"))
	C3 = int(raw_input("Area of C3:"))
	D1 = radiusOfCircle1(C1)
	D2 = radiusOfCircle2(C2)
	D3 = radiusOfCircle3(C3)
	Totals = (D1 + D2 + D3)

	print """ Circle	Diameter
c1 	{}
c2	{}
c3	{}
Totals	{}

""".format(D1, D2, D3, Totals)
main()


#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...

# Hint: Radius is the square root of the area divided by pi

