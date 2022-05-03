# Basic- Print all int from 0 to 150
for x in range(151):
    print(x)

# Multiples of Five- Print all the multiples of 5 from 5 to 1000
for x in range(5,1001,5):
    print(x)

"""
Counting, the Dojo Way-Print integers 1 to 100.
If divisible by 5, print "Coding" instead.
If divisible by 10, print "Coding Dojo"
"""
for x in range(1,101):
    if x%10==0:
        print("Coding Dojo")
    elif x%5==0:
        print("Coding")
    else:
        print(x)

# Whoa. That Sucker's Huge
# Add odd integers from 0 to 500,000, 
# Print the final sum.
sum =0
for x in range(1, 500001, 2):
    sum = sum + x
print(sum)

# Countdown by Fours
# Print positive numbers starting at 2018
# counting down by fours
for x in range (2018,0,-4):
    print(x)

# Flexible Counter
# starting at lowNum=1 till highNum=20 print out the multiple of 5
lowNum=1
highNum=21
mult=5

while lowNum < highNum: #while lowNum is less than 20
    if lowNum%mult==0: #if lowNum % 5 ==0
        print(lowNum) #print out the lowNum
    lowNum +=1
