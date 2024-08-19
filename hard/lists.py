# Lists
# Lists are stored variables able to hold a lot of data
# No more using singular variables
# [] are used to keep them

toys = ["Legos", "Action Figures", "Dolls", "Cars"]

nums = [1, 2, 10.5, 21]

print(toys)

# Iterating through lists with a for loop

'''

for toy in toys:
    # code to be repeated because of iteration

'''

for toy in toys:
    print(toys)
# for each toy in the toys lists it prints out 4 lists of the same list


# List index 
# Items in an index are assigned a number. It starts at 0

"""
            0           1               2       3
toys = ["Legos", "Action Figures", "Dolls", "Cars"]

"""


instruments = ["Guitar", "Trumpet", "Drums", "Violin", "Piano"]

strings = instruments[0]
# Using this can call the specific item from the list using the index
# You can also replace a specific item in the list using the index

instruments[0] = "Apple"

print(instruments[0])


# len()
# len is short for length
# it counts the number of items in the list and gives a integer

total = len(instruments)
print(total)



# Combining lists
# it can form a new list combining 2 lists together
# use the +

foods = ['pasta', 'steak', 'noodles', 'fried chicken']
drinks = ['water', 'soda', 'lemonade', 'beer']

meals = foods + drinks

# You can use if else statements to check if something is in the list

if "pasta" in foods:
    print("We got pasta!")
else:
    print("Sorry no pasta.")


# List methods
# List methods are special properties where we can manipulate what we want to do with lists
""" 
A list is a special type of data called an object. Objects are data types used to model things. 
which have attributes and have specific methods of interacting with them
"""
"""


object.attribute
# An attribute is utlized as a special data type to describe something

object.method(args)
# A method is utlized as a special function type to describe something

Use a period . then the follow attribute or method to utilize it
"""

.append()
# This adds an item at the end of a list
# Ex.
drinks.append("milk")


.remove()
# This removes an item from a list
# Ex.
drinks.remove("milk")