def multiply(x, y):
	z = x * y
	return z
	
def output(name, x, y, z, someone):
	return """
Hello {}
Because you were born on {} of the month {} you have {} days left until {} finds your salvation. 
""".format(name, x, y, z, someone)

def main():
	name = raw_input("Type your name: ") 
	x = raw_input("Type the day you were born: ")
	y = raw_input("Type the month you were born as a number: ")
	z = multiply(int(x), int(y))
	someone = raw_input("Type a famous person: ")
	print output(name, x, y, z, someone)

main() 
