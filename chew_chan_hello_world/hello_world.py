# 1. TASK: print "Hello World"
print( "Hello World" )

# 2. print "Hello Noelle!" with the name in a variable
name = "Chew"
print( "Hello", name )	# with a comma
print( "Hello " + name )	# with a +

# 3. print "Hello 42!" with the number in a variable
name = 42
print("Hello", int(name),"!")	# with a comma
print("Hello " + str(name) + " !") # with a + --Ninja Bonus: Python can add two strings together, set the num into string, then we will be able to "add" them together

# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "noodles"
print( "I love to eat {} and {}.".format(fave_food1,fave_food2) ) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.") # with an f string
# Bonus: Print with other string methods
# added the title() method, make the first letter capitalize
# added the capitalize () method, make the first letter capitalize
print(f"I love to eat {fave_food1.title()} and {fave_food2.capitalize()}.")
# center the fave_food1 with "^" both side.
x = fave_food1.center(20, "^")
print(x)


