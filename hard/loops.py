# Loops
# Loops are what they sound like, take a specific task to loop and keeping your code D.R.Y.
# While loops repeats a block of code that is true until it becomes false
# Each repeat is called an iteration

soccer_balls = 0

while soccer_balls <= 10:
    print(soccer_balls)
    soccer_balls = soccer_balls + 1


# incrementing and decrementing
"""
num = 0
num = += 1
adds current value from 0


num = 100
num -= 10
subtracts 10 from current value of 100
"""

num = 25
add = 1

while num < 10:
    print(f'{num} + {add}) = {num + add}')
    num += 1



# For loops
# A for loop is a programming construct that repeatedly executes a block of code until a condition is met

nums = range(0, 20, 2)

for c in range(1, 10):
    print(c)


# Break statements
# Break statements skips the rest  of the remaining loop iterations exiting the loop early and used for specific conditions

'''
for c in range(1, 10):
    if == 5:
        break


# Continue Statement

for c in range(1, 10):
    if == 5:
        print("Hello World!")
        continue

'''


# Making a tree

leaf = 0

for leaf in range(1, 6):  
    leaf = leaf * 2 - 1  
    print(f'{" " * (5 - leaf // 2)}{"#" * leaf}')
print(f'{" " * 4} ||')