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