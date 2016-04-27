def countup(n):
	if n >= 10:
		print "Blastoff!"
	else:
		print n
		countup(n+1)



def main():
	countup(1)


main()

def countdown_from_to(start,stop): 
	if start == stop:
		print "Blastoff!"
	elif start <= stop:
		print "Invalid pair"
	else: 
		print start
		countdown_from_to(start - 1,stop)
	
def main():
	countdown_from_to(89,53)

main()

def adder(sum_):
	number = raw_input("Next Number") 
	if (number) == "":
		print "The Sum Is {}".format(sum_)
	else:
		print
		sum_ += int(number)
		adder(sum_)


def main():
	adder(0) 
main()

