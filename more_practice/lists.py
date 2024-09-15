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


# Accessing items
fruits = ['banana', 'orange', 'mango', 'lemon'] 
last_fruit = fruits[-1]
second_last = fruits[-2]
print(last_fruit)       
print(second_last)   

# Slicing items
fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[0:4]
all_fruits = fruits[0:] 
orange_and_mango = fruits[1:3] 
orange_mango_lemon = fruits[1:]

fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[-4:] 
orange_and_mango = fruits[-3:-1]
orange_mango_lemon = fruits[-3:]


fruits = ['banana', 'orange', 'mango', 'lemon'] 
fruits[0] = 'Avocado' 
print(fruits)     
fruits[1] = 'apple'
print(fruits)     
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)     

# checking items
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  
does_exist = 'lime' in fruits
print(does_exist) 
