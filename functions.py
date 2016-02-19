def add(a, b):
	return a + b
#defines a function

add(3, 4)
#defines function to add

def sub(a, b):
	return a - b

sub(5, 3)
#defines functions to subtract

def mul(a, b):
	return a * b

mul(4, 4)
#defines functions to multiply

def div(g,h):
	return g/h

div(2, 3)
#defines function to divide numbers 

def SecsToHours(a,b,c):
	return a/b/c

SecsToHours(86400,60,60) 
#converts number of seconds into hours
def Areaofacircle(r):
	pi = (math.pi)
	return pi * r**2
	
Areaofcircle=(5)
#tells the area of a circle
def Volumeofsphere(r):
	pi = (math.pi)
	return (((4/3.0)*pi)*r**3)

Volumeofsphere=(5)
#tells the volume of a sphere
def averagevolume(a,b):
	pi = (math.pi)
	Vol1 = (((4/3.0)*pi)*a**3)
	Vol2 = (((4/3.0)*pi)*b**3)
	return Vol1 + Vol2/2

averagevolume(5,10)
#tells the average voulume of two spheres
def areaoftriangle(a,b,c):
	p = a+b+c/2.0
	return math.sqrt(p*(p-a)*(p-b)*(p-c))

areaoftriangle(1,2,2.5)
#tells the area of a triangle

def right_align(a):
	return (a.rjust(80))
right_align("Hello")
#aligns hello to the right side of python
def center(a):
	return (a.center(40))
center("Hello")
#aligns hello to center of python
def msgbox(a):
	x =    """		  +---------+
		  |  """+"Hello"+"""  |
		  +---------+"""
	print x
	return"""		  +---------------+
		  |  """+a+"""  |
		  +---------------+"""
	
print msgbox("I eat cats!")
# displays the word Hello and I eat cats! in a box

 a = add(4,3)
 s = sub(9,2)
 m = mul(4, 4)
 d = div(8,4)
 h = SecsToHours(86400,60,60) 
 c = Areaofcircle=(5)
 v = Volumeofsphere=(5)
 t = areaoftriangle(1,2,2.5)
#calls each of the functions

print msg_box(a)


 
 

 
 
