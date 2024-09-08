# 4 types of data collection types in python
# List: ordered and changeable(modifiable) values into a collection data type, it allows duplicate members
# Tuple: same thing as a list however it is unchangeable or unmodifiable(immutable)
# Set: a unordered, un-indexed and unmodifiable
# Dictionary: unordered, changeable and indexed. No duplicate members

# These data collection types are used and referred to store values in large scale to be used again and again. Say for example hundreds of thousands of employees information in a data base to be used.

empty_list = list() # no item in the list
print(len(empty_list)) # 0


shoes = ['Adidas', 'Nike', 'Vans', 'Skechers', 'Sneakers']
countries = ['USA', 'Canada', 'Mexico', 'China', 'Russia']
clothing = ['T-Shirt', 'Hoodie', 'Turtle-neck', 'button up shirt']


# Print the lists and it length
print('shoes:', shoes)
print('Number of fruits:', len(shoes))
print('Number of countries:', len(countries))
print('Clothing:', clothing)
print('Number of clothing:', len(clothing))
print('Number of countries:', len(countries))

# Modifying list

shoes = ['crocs', 'vans', 'gucci', 'Skechers'] 
first_shoes = shoes[0] 
print(first_shoes)   
second_shoes = shoes[1]
print(second_shoes)  
last_shoes = shoes[3]
print(last_shoes) 
last_index = len(shoes) - 1
last_fruit = shoes[last_index]

