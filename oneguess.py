import random
def numberRange(number1, number2):
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
	result = int(numberRange(number1,number2))
	wrong = resultbyuser(result,usersGuess)
	if result == usersGuess:
		print """The number was {}
Your guess was {}
You are correct! I don't know how but woowowoowowoowowowowowowoowowowowowowoowowowowowoowowow, you're cool.""".format(result,usersGuess)
	else:
		print """The number was {}
Your guess was {}
{}""".format(result,usersGuess,wrong)

main()

