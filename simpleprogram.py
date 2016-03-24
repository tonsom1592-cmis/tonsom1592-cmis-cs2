def multiply(x, y):
	daysLeft = dayBorn * monthBorn
	return daysLeft
	
def output(name, dayBorn, monthBorn, daysLeft, someone):
	return """
Hello {}
Because you were born on {} of the month {} you have {} days left until {} finds your salvation. 
""".format(name, dayBorn, monthBorn, daysLeft, someone)

def main():
	name = raw_input("Type your name: ") 
	dayBorn = raw_input("Type the day you were born: ")
	monthBorn = raw_input("Type the month you were born as a number: ")
	daysLeft = multiply(int(x), int(y))
	someone = raw_input("Type a famous person: ")
	print output(name, dayBorn, monthBorn, daysLeft, someone)

main() 
