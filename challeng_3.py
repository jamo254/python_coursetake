# Given an inRange(x, y) function, 
# write a method that determines whether a given pair(x, y) falls in the range(x < 1/3 < y). 
# Essentially, you’ll be implementing the body of a function that takes in two numbers x and y and returns True if x < 1/3 < y
# otherwise, it returns False.

#checking whether true or false

def inRange(x, y):
    return (x < 1/3 < y)
print(inRange(3, 4))


# s = s[:position_to_insert] + char_to_insert + s[position_to_insert:]?\
        
