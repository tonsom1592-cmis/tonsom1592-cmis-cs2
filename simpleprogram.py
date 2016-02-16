def multiply(x, y):
	z = x * y
	return z
	
def output(name, x, y, z):
	return """
Hello {}
Did you know:
{} * {} = {}
""".format(name, x, y, z,)

def main():
	name = raw_input("Type your name: ") 
	x = raw_input("Type a number: ")
	y = raw_input("Type another number: ")
	z = multiply(int(x), int(y))
	print output(name, x, y, z)

main() 
