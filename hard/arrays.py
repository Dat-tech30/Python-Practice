# Practice using arrays
# Arrays are like lists, however with storing values and know is in place an array differs from a list by being treated as a larger version of a list
# Being memory-efficient and has faster operation speeds
# And to use an array is you use the module and import it


# Example from GeeksforGeeks

import array as arr
a = arr.array('i', [1, 2, 3])
print("The new created array is : ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")
print()
b = arr.array('d', [2.5, 3.2, 3.3])
print("\nThe new created array is : ", end=" ")
for i in range(0, 3):
    print(b[i], end=" ")

# This imports the array module so you'll be able to use arrays
import array as arr

# This is making the letter "a" an array with the function arr.array that can only store integers ('i' stands for signed integers) it establishes with the elements being 1, 2, 3
a = arr.array('i', [1, 2, 3])

# Its just printing "The new created aray is :" with end=" " which keeps cursor on the same code line
print("The new created array is : ", end=" ")

# This is creating a for loop for i in range of 0, and 3
# The for loop runs from i = 0 to i = 2 (3 iterations in total).
# In each iteration, a[i] accesses the element at index i in the array a.
# print(a[i], end=" ") prints each element followed by a space, without moving to a new line.
for i in range(0, 3):

# Moving to a new line
print()
    
# The code after does the same thing

'''

Summary
The code first creates an integer array and prints its elements.
Then, it creates a floating-point array and prints its elements.
The use of for loops and print statements with end=" " ensures that all elements of the arrays are printed on the same line, separated by spaces.

'''