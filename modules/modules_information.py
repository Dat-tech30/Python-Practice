# Python has a lot of built in functionality
# Some of the functionality can be accessed in libraries called Modules

# Using those modules you would have to "import" it
# For example the Python random module contains functions for generating random values, such as integers, and floats, or rearranging data

import random
# importing the module

from random import randint
# this imports a specific function

# randint() function

num = randint(1, 1000)
# randint() function generates random integers from a range of numbers


for num in range(1, 1000):
    print(num)
    if num == 38:
        print("It finished!")
        break