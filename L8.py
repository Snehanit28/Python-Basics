# Functions 

# Module functions

# import math
# print(dir(math))      # =>from this we can see all the functions in math module
                        # => select the 'sqrt' function from the math module

from math import sqrt   # from this we select the 'sqrt' function
print(sqrt(16))         # Output: 4.0

from math import *      # import all functions from the math module
print(sqrt(25))         # Output: 5.0
print(pow(2, 3))        # Output: 8.0
print(factorial(5))     # Output: 120

#User-defined functions

def sum(a, b):
    print(a + b)
print(sum(5, 10))  # Output: 15
