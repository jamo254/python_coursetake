# python_coursetake
Data Structures and algorithms in Python


```python

# Lists are created using square brackets[]
l = [1, 4, 5, 12, 45]
print('Lists = ', l)
print(l[0])
print(l[1])

# Sublist
# Sometimes you want just a small portion of a list—a sublist. Sublists are simply subsets of a list
# they can be retrieved using a technique called slicing.

# Given a list l, to create sublist l1 and l2 write:
l = [3, 5, 4, 6, 42, 22]
l1 = l[0:3]
l2 = l[3:5]

print(l1, l2)

# Iterating lists using for
l = [2020, 2030, 2040, 2050]
for i in l:
    print("Year: ", i)

# Given a getSublist() function, create a list named l[1, 4, 9, 10, 23]. Using list slicing, get the sublists[1, 4, 9] and [10, 23].

# Input
# A list

# Output
# Two sublists


def getSublist():
    l = [1, 4, 9, 10, 23]
    list_1 = l[0:3]
    list_2 = l[3:]
    return[list_1, list_2]


[list_1, list_2] = getSublist()

print("List 1:", list_1)
print("List 2:", list_2)

# Given an AppendtoList() function, create a list named l with the following values:
# [1, 4, 9, 10, 23]
# and appends the number 90 at the end of the list.
# Input
# A list of numbers
# Output
# Append the value 90 to the end of the list l
# Sample Input
# [1, 4, 9, 10, 23]
# Sample Output
# [1, 4, 9, 10, 23, 90]


def AppendtoList():
    l = [1, 4, 9, 10, 23]
    l.append(90)
    return l


print(AppendtoList())

# Given a getAverage() function, create a list named l with the following values:
# [1, 4, 9, 10, 23]
# Calculate the average value of all values in the list.
# Input
# A list of integers
# Output
# An average of values in the list
# Sample Input
# [1, 4, 9, 10, 23]
# Sample Output
# 9.4


def getAverage():
    l = [1, 4, 9, 10, 23]
    average = sum(l) / len(l)
    return average


print('Average = ', getAverage())

# Remove Sublist From List
# Can use remove()


def removeList():
    l1 = [1, 4, 9, 10, 23]
    l2 = [4, 9]
    l1.remove(l2[0])
    l1.remove(l2[1])
    return l1


l1 = removeList()
print(l1)


def removeFromList():
    l1 = [1, 4, 6, 7, 7, 8]
    l2 = [4, 6]
    l1.remove(l2[0])
    l1.remove(l2[1])
    return l1


l1 = removeFromList()

print(l1)


# List Comprehensions
# List comprehensions are a concise way to create lists.
# They consist of square brackets containing an expression followed by the for keyword
# the result will be a list whose results match the expression.

print([x*x for x in [1, 2, 3, 4, 3, ]])

# Using Raneg
print(x*x for x in range(4))  # Output - [1, 4, 9, 16, 9]
# The following python code displays all elements from 0 to 9 which are divisible by 2.
print([x*x for x in range(10) if x % 2 == 0])

# Challenge 5: List of Squares
# Given a getSquare() function, create a list with the squares of the first 10 numbers, i.e., in the range from 1-10.
# Input
# An empty list
# Output
# An updated list with the square of each value in the list


def getSquare():
    # Write your code here
    l1 = [x*x for x in range(11) if x != 0]  # Create your list here
    return l1


l1 = getSquare()
print(l1)


def getSquareTwo():
    l1 = [x*x for x in range(1, 11)]
    return l1


print(getSquareTwo())

# Challenge 6: - List of Cubes


def getCube():
    l1 = [x**3 for x in range(21) if x != 0]  # range(1,21)
    return l1


print(getCube())

# Challenge 7: Lists of Even and Odd Numbers
# In this challenge, you are required to create a list containing even and odd numbers.
# Input
# Two empty lists
# Output
# List 1 with even numbers
# List 2 with odd numbers


def ListofEvenOrOdd():
    l1 = [x for x in range(0, 20) if x % 2 == 0]
    l2 = [x for x in range(1, 21) if x % 2 != 0]
    return [l1, l2]


[l1, l2] = ListofEvenOrOdd()

print('Lists even numbers:', l1)
print('List odd numbers:', l2)

# Challenge 8: Sum of Squares of Even Numbers
# In this challenge, your task is to create a list of the squares of even numbers.
# Input
# A list with the square of even numbers from 0-20
# Output
# The sum of the numbers in the list

def evenSquare():
    l1 = [x*x for x in range(0,20) if x % 2 == 0]
    return sum(l1)

print("Even squared numbres:", evenSquare())

# Even Squares Not Divisible By Three
# Use a list comprehension that iterates over a range of 0-21, 
# increments the number in the range by 2 and squares each remaining number. 
# Also, use a predicate clause to check if the squared number is not divisible by 3, 
# then put the number in the list.

def divisibleByThree():
    l1 = [x*x for x in range(0, 21, 2) if x % 3 != 0]
    return l1

print(divisibleByThree())
```














