first_name = 'Dat'
last_name = 'Phan'
state = 'washington'
age = '500'
is_married = 'false'
hobbies = ['anime', 'videogames', 'music', 'driving', 'food']
info = {
    'age': '500',
    'eye-color': 'black',
    'state': 'WA',
    'height': '8\'0 ft'
}

# Printing the values stored in the variables


print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('state: ', state)
print('age: ', age)
print('Married: ', is_married)
print('Info: ', info)


# Declaring multiple variables in one line

first_name, last_name, state, age, is_married = 'Dat', 'Phan', 'Washington', 500, False

print(first_name, last_name, state, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('State: ', state)
print('Age: ', age)
print('Married: ', is_married)