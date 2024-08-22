# Dictionaries are better versions of lists able to store thousands of data including able to key and value data
# This means a keyed, mutable collection of values

animals = {
    "Tiger" : "Jungle",
    "Shark" : "Ocean",
    "Frog" : "River",
    "Scorpiopn" : "Desert",
    "Polar Bear" : "Antartica"
}


# Getting a value from a dictionary using the key
# To access a value, we use [] just like how we acess a value in a list

"""

customer = {
    'name' : 'Mary Jane',
    'email' : 'MJ@janesmith.com',
    'phone' : '555-555',
}

email = customer['email']

"""


# We can also replace a value in a dictionary using the key

"""
customer = {
    'name' : 'Mary Jane',
    'email' : 'MJ@janesmith.com',
    'phone' : '555-555',
}

customer['email'] = "MJ@gmail.com"

"""

# Same goes for adding a new key-value pair to the dictionary


"""

customer['address'] = "1222 S Main St."

"""


print(f"A Tiger lives in a {animals['Tiger']}.")
print(f"A Frog lives in a {animals['Frog']}.")


# We can also remove a key-value pair from a dictionary with a .pop()

animals.pop('Polar Bear')


# We can also iterate through a dictionary
# For each key use a for loop to run code for each key in a dictionary

for key in animals: 
    print(animals)


# Iterating through values with .values()
# Use this method to only iterate through the values

# To get access to both the key and values, use
# 2 iteration variables separated by a , comma
# the .items() method

for key,value in animals.item():
    # Code to run


# We can also have separate files to store our huge dictionaries to import onto our main file
# to code

# ex.

# from animal import animals
# Don't import it from the original file like this:
# animals.py

# No symbols, just names. No file extensions. And no bracket syntax.