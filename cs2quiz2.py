#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#a) True
#b) False
#c) Object == True
#
#2) What does 'return' do?
# It gives a final value of the function's calculation

#3) What are 2 ways indentation is important in python code?
#a) If you don't indent your lines properly, your program won't work because python won't recongize what lines are part of the function. 
#b) Organizes the code to what function is it a part of 

#PART 2: Reading
#Type the values for 12 of the 16 of the variables below.
#
#problem1_a) = -36
#problem1_b) = -(math.sqrt(3))
#problem1_c) = -(math.sqrt(0))
#problem1_d) = -5
#
#problem2_a) = True
#problem2_b) = False
#problem2_c) = False
#problem2_d) = False
#
#problem3_a) = 0.03
#problem3_b) = 0.05
#problem3_c) = 0.5
#problem3_d) = 0.25
#
#problem4_a) = 7
#problem4_b) = 5
#problem4_c) = 0.125
#problem4_d) = 5
#

#PART 3: Programming
#Write a script that asks the user to type in 3 different numbers.
#If the user types 3 different numbers the script should then print out the
#largest of the 3 numbers.
#If they don't, it should print a message telling them they didn't follow 
#the directions.
#Be sure to use the program structure you've learned (main function, processing function, output function)


def comparing(number1,number2,number3):
   if number1 > number2 and number1 > number3 == float or int:
       return number1



   elif number2 > number1 and number2 > number3 == float or int:
       return number2



   elif number3 > number1 and number3 > number2 == float or int:
       return number3
   else:
       return " You didn't follow the instuctions "



def output(Values):
   if Values == " You didn't follow the instuctions ":
       out =  " You didn't follow the instructions "   
   elif Values == float or int:
       out = "The largest number was {}".format(Values)
   else:
       print " You didn't follow the instructions "
   print out



def main():
   print "Type in three different numbers(decimals are Ok!)"
   number1 = raw_input(" A: ")
   number2 = raw_input(" B: ")
   number3 = raw_input(" C: ")
   Values = comparing(number1,number2,number3)
   result = output(Values)



main()

