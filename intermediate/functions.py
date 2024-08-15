# def function
# the define function is reusable block of code, like a mathematical equation you always refer back or reuse every time
# You first define it then call it

def pets (): #have this colon
    print('I love my dog!')
    #Run your code
    #Make sure to indent

# then you call the function to run
pets()

# Rules for naming functions
# No SPACES
# No starting with NUMBERS
# No special characters except _
'''ex.

def the func():
def 21():
def pets??():

'''

# Correct ways:

# def the_func():
    #code
# def func21():
    #code
# def func():
    #code

# PRACTICE

def electronic_pricing():
    camera = 59.99
    modem = 70.99
    router = 120.99
    monitor = 159.99
    tax = 2.99
    c_value = float(camera)
    r_value = float(router)
    print('Hey welcome back to the shop! What\'re you looking to buy?')
    print(f'We have this awesome camera ${c_value} and a router ${r_value}!')
    print("Oh great your buying those? Great choice let me ring you up!")
    total = c_value + r_value + tax
    print(f'You\'re total is ${total}')


electronic_pricing()




# Keep yourself DRY (Do not Repeat Yourself!)
# Keep your code clean and concise

# Global variables are available to functions and other parts of a program
# Local variables are only available to the functions inside which they're created

'''Ex. of how to keep it clean and concise

#Global variables
pet = "Dog"
pet_2 = "Cat

#Functions
def func():
    print(pet)

#Function calls
func()

'''