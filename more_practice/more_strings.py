# Ex.
# Slicing Python strings
language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon




# Practice

fruit = "banana"
slicing_fruit = fruit[0:2]
print('I sliced the banana into', slicing_fruit)


# returing the index of first occurence of substring

fruits = "Apples, Oranges, Watermelon"
print(fruits.find('a'))
print(fruits.find('A'))


# Unpacking characters

coding_language = "JavaScript"

a, b, c, d, e, f, g, h, i, j, = coding_language
print(a)

print(f'in the word {coding_language} there is the letter', a ,'in it')



# There is so many strings methods and functions - I can't cover all of them however if I would like to check it out I can go to geekforgeeks or look it up!
