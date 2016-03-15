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

