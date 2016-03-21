import random
def numberRange(number1, number2)
	return random.randint(number1, number2)

def resultbyuser(result,usersGuess):
	if result > usersGuess:
		sub = abs(usersGuess - result)
		return "That's over by {}".format(sub)
	else:
		add = abs(usersGuess + result) 
		return "That's under by {}".format(add)

def main(): 
	number1 = int(raw_input("What is the minimum number?"))
	number2 = int(raw_input("What is the maximum number?"))
	print "I'm thinking of a number from {} to {}".format(number1 , number2)
	usersGuess = int(raw_input("What do you think it is?:"))
	result = int

