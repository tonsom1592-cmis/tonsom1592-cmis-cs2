def multiply(x, y):
	return x * y

def output(name, thinking, doing, x, y, z, elections):
	out = """

Hello {},
The meaning of life is {} because you {} too hard
Also, you have {} * {} = {} days until {} will help you find your salvation. 
Have a good day!
""".format(name, thinking, doing, x, y, z, elections)
	return out

def main():

	name = raw_input("Type your name:")
	thinking = raw_input("What are you thinking about right now?:")
	doing = raw_input("What do you like to do?:")
	x = raw_input("Type your age in years:")
	y = raw_input("Type the day you were born. Just the day:")
	z = multiply(int(x), int(y))
	elections = ("Who do you thinking will win the elections, Donald Trump or Kanye West?:") 
	
	out = output(name, thinking, doing, x, y, z, elections)
	print out
main()
