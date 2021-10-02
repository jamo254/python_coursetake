# Check Parity of a Number - 
# In this challenge, you have to calculate the parity of a number.

# Sample Input
# 4

# Sample Output
# 0
#checking whether a number is even 

def checkParity(number):
    #check if even
    
    if number:
        return number % 2
print('number:', checkParity(8))
print('number:', checkParity(6))
print('number:', checkParity(7))
print('number:', checkParity(11))


    

