import random
import math
#This is an interactive music game
#Quizzes you questions relating to music
print """ Welcome to The Interactive Music Game!
	You will answer questions relating to music. Let's begin: """
def  caughtInALandSlide():
	print "Type the choice with the correct song lyrics: Caught in a landslide _______"
	a = "a: I took a pill in Ibiza, to show Avicii I was cool"
	b = "b: No escape from reality"
	c = "c: Lately, I've been, I've been losing sleep"
	print a
	print b
	print c

	userinput = raw_input("Pick a, b or c: ")  
	if userinput == "b" : 
		print "You are correct!"
	else:
		print "That's the wrong lyrics :("

def greenDay():
	print "Greenday's __ Guns"
	number = raw_input("Insert the correct number of the song title: ")
	if number == "21": 
		print "You are correct"
		print "Greenday's {} Guns".format(number)
	elif number < "21":
		print "That's too low"
	elif number > "21":
		print "That's too high"


def britneySpeares():
	number = int(raw_input("What year did Britney Speares have her famous meltdown?: "))
	if number == 2007:
		print "That's right! May we never forget"
	elif number < 2007:
		print "That's too early. She was still sane back then"
	elif number > 2007:
		print "That's too late. She bounced back."

def sweetDreams():
	print "Who originally wrote Sweet Dreams?: "
	a = "a: Eurythmics"
	b = "b: Marylin Manson"
	c = "c: Emily Brown"
	print a
	print b
	print c

	userinput = raw_input("Pick a, b or c: ")  
	if userinput == "a" : 
		print "You are correct!"
	else:
		print "You are incorrect"

def deepPurple():
	print "Who were the lead singers of Deep Purple?"
	firstM = raw_input("Who was the first lead singer of Deep Purple?")
	secondM = raw_input("Who replaced that lead singer?")
	if firstM == "Rod Evans" and secondM == "Ian Gillan":
		print "That's correct!"
	elif firstM == "Rod Evans" or secondM == "Ian Gillan":	
		print "You got one correct"
	elif not firstM == "Rod Evans" and not secondM == "Ian Gillan":
		print "You are incorrect"
	else: 
		print "You are incorrect"
def bonusRound():
	number1 = random.random()
	number2 = random.randint(0,45)
	q1 = "sum {}".format(number2)
	print q1
	guess1 = raw_input("Is this the number of the band?")
	if guess1 == "yes" and number2 == 41:
		print "That's correct!"
	elif guess1 == "no":
		print "Correct, the band number is 41"
	else: 
		print "That's wrong"
	guess2 = raw_input("Bonus question: What number am I thinking of between 0 and 1?")
	if guess2 == "" : 
		print "That's incorrect. Thanks for playing!" 
		return "There is no right answer" 
	
def main(): 
	caughtInALandSlide()
	greenDay()
	britneySpeares()
	sweetDreams()
	deepPurple()
	bonusRound()
main()
