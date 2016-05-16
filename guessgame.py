import random 
def check(number,rAndom,rounds):
	if int(number) == rAndom and rounds == 2 or 3:
		rAndom = random.randint(0,100)
		attempts(rounds-1,rAndom,tries=5)
	elif rounds <= 0:
		print "Thanks for playing "
	else:
		print "Thanks for playing "

def guess(rounds,rAndom,tries):
	number = raw_input("Guess a number: ")
	if int(number) == rAndom:
		print "Thats correct!"
		print "{} rounds remaining".format(rounds)
		check(number,rAndom,rounds)
	elif int(number) < rAndom:
		print "That's too low "
		attempts(rounds,rAndom,tries-1)
	elif int(number) > rAndom:
		print "That's too high "
		attempts(rounds,rAndom,tries-1)
	else:
		print "Do you want to play a game? "

def attempts(rounds,rAndom,tries):
	if rounds == 0 and tries == 0:
		print "Thanks for playing!"
		exit()
	if tries == 0:
		print "{} rounds remaining".format(rounds)
		tries = 5
		rAndom = random.randint(0,100)
		guess(rounds-1,rAndom,tries)
	else:
		guess(rounds,rAndom,tries)

def main():
	print "Guess a number from 0 to 100. You have 5 tries in each round"
	print "{} rounds remaining".format(3)
	rAndom = random.randint(0,100)
	rounds = 2
	tries = 5
	attempts(rounds,rAndom,tries)
main()	
