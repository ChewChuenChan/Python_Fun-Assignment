# variable num1 & num2 declaration, initialize numbers
""" numb1; storing an int
num2 storing a float """
num1 = 42
num2 = 2.3

# variable boolean declaration, initialize boolean to value TRUE
boolean = True

# variable string declaration, initialize string as "Hello World"
string = 'Hello World'

# variable declaration, initialize list
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
# variable declaration, initialize dictionary
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
# variable declaration, initialize tuple
fruit = ('blueberry', 'strawberry', 'banana')

"""
log statement; type check
In this case output will be tuple
"""
print(type(fruit))
# log statement; access value from list
# access the pizza_toppings with index of 1 and print value
print(pizza_toppings[1])
# add value to list
pizza_toppings.append('Mushrooms')
# log statement; access value from dictionary
# print the person's 'name' value out
print(person['name'])
# change value from dictionary
# change person's 'name' value to 'George'
person['name'] = 'George'
# add a new key value to dictionary
person['eye_color'] = 'blue'
"""
log statement; access value from tuple
TypeError: 'tuple' object does not support item assignment
"""
print(fruit[2])

"""
conditional statement:if, else if, else
"""
if num1 > 45: #if num1 is greater than 45
    print("It's greater") #print "It's greater"
else: #otherwise, print "It's lower"
    print("It's lower") #output will be "It's lower" because num1 is 42

if len(string) < 5: #if string length is less than 5
    print("It's a short word!") #print "It's a short world!"
elif len(string) > 15: #if string length is greater than 15
    print("It's a long word!") #print "It's a long word!"
else: #if 5< string length <15 , print "Just right!"
    print("Just right!") #output will be "Just right!" because string lenght is 7 for "Hello World" 

# for loop
for x in range(5): # start at 0; stop at 5, 1 increment
    print(x)
for x in range(2,5):# start at 2; stop at 5, 1 increment
    print(x)
for x in range(2,10,3): # start at 2; stop at 10, 3 increment
    print(x)
# variable x declaration; initial value x to 0
x = 0 #start when x=0
# while loop
while(x < 5): # stop when x is 5
    print(x) # print the while
    x += 1 #increment

#delete value from pizza_toppings list
pizza_toppings.pop() 
#delete value from pizza_toppings list with number index 1
pizza_toppings.pop(1)

#log statement, print dictionary 'person' out
print(person)
#delete value 'eye_color' from dictionary 'person'
person.pop('eye_color')
# log statement, print dictionary 'person' out
print(person)

# for loop in list 'pizza_toppings', start from index 0 till finish,
# in this case it will 4 times, cause 1 value has deleted. 
for topping in pizza_toppings:
    if topping == 'Pepperoni': #set if condition, if topping has 'pepperoni'
        continue
    print('After 1st if statement')# print 'after 1st if statement'
    if topping == 'Olives': # set if condition, if toppitng shows 'olives'
        break# stop

#function print_hello_ten_times declaration
def print_hello_ten_times():
    for num in range(10): # this fuction will print "Hello" 10 times
        print('Hello')

print_hello_ten_times() #call the function

def print_hello_x_times(x):
    for num in range(x): # set parameter into x
        print('Hello')

print_hello_x_times(4) # call the function by setting parameter into 4

def print_hello_x_or_ten_times(x = 10): # declare function, set parameter x =10
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() |#call the fuction, this will print out 10 "Hello"
print_hello_x_or_ten_times(4) #call the funtion, this will print out 4 "Hello"


"""
Bonus section
"""

# print(num3)
# num3 = 72

# TypeError: 'tuple' object does not support item assignment
# fruit[0] = 'cranberry'

# KeyError: 'favorite_team'
# print(person['favorite_team'])

# IndexError: list index out of range
# print(pizza_toppings[7])

# IndentationError: unexpected indent
#   print(boolean)

# AttributeError: 'tuple' object has no attribute 'append'
# fruit.append('raspberry')

# AttributeError: 'tuple' object has no attribute 'pop'
# fruit.pop(1)