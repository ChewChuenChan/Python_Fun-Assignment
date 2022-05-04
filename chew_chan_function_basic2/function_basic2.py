# Countdown
# Create a function that accepts a number as an input. 
# Return a new list that counts down by one, 
# from the number (as the 0th element) down to 0 (as the last element).

# def countdown(n):
#     list1=[]
#     for x in range (n,-1,-1):
#         list1.append(x)
#     return list1

# call function and print output
# print(countdown(5))


# Print and Return
# Create a function that will receive a list with two numbers. 
# Print the first value and return the second.

#  def print_and_return(list):
#     print (list[0])
#     return list[1]

# call function and print output
# print(print_and_return([1,2]))


#First Plus Length
# Create a function that accepts a list 
# and returns the sum of the first value in the list plus the list's length.

#  def first_plus_length(list):
#     return list[0] + len(list)

# call function and print output
# print(first_plus_length([1,2,3,4,5]))

#Values Greater than Second
# Write a function that accepts a list and creates a new list containing 
# only the values from the original list that are greater than its 2nd value. 
# Print how many values this is and then return the new list. 
# If the list has less than 2 elements, have the function return False

def values_greater_than_second(list):
    if len(list) < 2:
        return False
    else:
        list4 = []
        for x in range (0,len(list)):
            if list[x] > list[1]:
                list4.append(list[x])
        print(len(list4))
        print(list4)
        return list4

# call function and print output
values_greater_than_second([5,2,3,2,1,4])
values_greater_than_second([3])
