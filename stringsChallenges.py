# Given an inRange(x, y) function,
# write a method that determines whether a given pair(x, y) falls in the range(x < 1/3 < y).
# Essentially, you’ll be implementing the body of a function that takes in two numbers x and y and returns True if x < 1/3 < y
# otherwise, it returns False.

# checking whether true or false

def inRange(x, y):
    return (x < 1/3 < y)


print(inRange(3, 4))

# Given a getStr() function,
# write the necessary sequence of operations to transform the string(containing three literals)
# in such a way that every literal is tripled​ respectively.

# Input
# A string

# Output
# Triple of every string literal

# Sample Input
# abc

# Sample Output
# aaabbbccc

# s = s[:position_to_insert] + char_to_insert + s[position_to_insert:]


def getStr(s):
    s = s[:1] + s[0] + s[1:]
    s = s[:1] + s[0] + s[1:]
    s = s[:3] + s[3] + s[3:]
    s = s[:3] + s[3] + s[3:]
    s = s[:6] + s[6] + s[6:]
    s = s[:6] + s[6] + s[6:]
    strlen = len(s)
    return [s, strlen]


print(getStr('abc'))  # output -> aaabbbccc

# Input
# A string

# Output
# The first occurrence of “b” and “ccc” in the string

# Sample Input
# aaabbbccc

# Sample Output
# [3, 6]


def findOccurence(s):

    b = s.find('b')
    c = s.find('c')
    return [b, c]


print(findOccurence('Iam a boy not a cat'))


# Problem Statement
# Given a function changeCase(s), the task is to convert the strings from upper case to lower case.

# Input
# A string in upper case

# Output
# Change case of the string in lower case

# Sample Input
# “AAA BBB CCC”

# Sample Output
# “aaa bbb ccc”
def changeCases(s):
    a = s.upper()
    b = s.lower()
    return[a, b]


print(changeCases("aaaaa, BBAMAJ"))
