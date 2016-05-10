import random
import math
print """ Welcome to The Interactive Music Game!
	You will answer questions relating to music. Let's begin: """
def  caughtInALandSlide():
	print "Type the choice with the correct song lyrics: Caught in a landslide _______"
	a = "a: I took a pill so Avicii would think I'm cool"
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
	number = raw_input("What year did Britney Speares have her famous meltdown?: ")
	if number == "2007":
		print "That's right! May we never forget"
	elif number < "2007":
		print "That's too early. She was still sane back then"
	elif number > "2007":
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

	
def main(): 
	caughtInALandSlide()
	greenDay()
	britneySpeares()
	sweetDreams()
	
main()


