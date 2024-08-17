# Boolean values are true or false statements
# Boolean values in python are capitalized

dog = True
cat = False

# if else statements are what they sound
# conditional statements but in python to be used to find something is true or false given a value

pet = False

if pet:
    print("This is a pet")
else:
    print("This is not a pet")

pet2 = True

if pet2:
    print("This is a pet")
else:
    print("This is not a pet")


# Conditional statements can get really specific if you need to check something
# Comparison operators:
'''
greater than >
less than <
greater than or equal >=
less than or equal <=
value equal ==
not equal !=
'''

chip_bags = 10

if chip_bags >= 10:
    print("That\'s a lot of chips you got there!")
else:
    print("You don\'t got that much chips.")


chip_bags1 = 9

if chip_bags1 >= 10:
    print("That\'s a lot of chips you got there!")
else:
    print("You don\'t got that much chips.")



# Using the value equal

chips = "BBQ"

if chips == "BBQ":
    print("Woah you got BBQ Chips? Can I have some?")
else:
    print("Oh it's not BBQ Nevermind.")

# elif statements
"""
elif (short for "else if") is used to check additional conditions in a 
sequence after an initial if statement and before an optional else statement, 
allowing for multiple branches in conditional logic.
"""

videogames = "rpg"

if videogames == "rpg":
    print("Hey wanna play that rpg game?")
elif videogames !="rpg":
    print("ah it\'s alright we can play something else")
elif videogames == "Food":
    print("Let\'s just get some food!")
else:
    print("Nevermind I think I\'m gonna go home.")


# We can also chain as much conditions as we need to!
# nested if statements
# nested if statements are if 2 conditions are true they can be together

temperature = 70

if temperature >= 70:
    if temperature < 90:
        print("Hey the weather is looking nice today! Lets go outside.")
    else:
        print("The weather is a little bit hot let\'s go the pool!")

