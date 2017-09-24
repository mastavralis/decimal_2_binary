# -*- coding: utf-8 -*-
"""
Author: Dionisis Mastavralis
Github URL: https://github.com/mastavralis/decimal_2_binary

This function takes any decimal number
as input and converts it into binary number.
"""

# create an empty list
binary = []

# convert any decimal number to binary
def decToBinary(n):
    
    if(n == 0): # this is the base case
        # we are done
        binary_string = ''.join(map(str, list(reversed(binary))))
        print(binary_string)
    else:
        m = n % 2 # find the remainder between n % 2
        x = n / 2 # divide n by two to continue the sequence
        binary.append(m) # append the result of the division in to the list
        decToBinary(x) # recall function recursively
    

# call the function with any decimal number as input
decToBinary(88)
