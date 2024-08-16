# The () function can be called for sending data to the function. This is called an argument
# Parameters allow the function to accept the data
# Parameters are the variables set by the arguments
# parameter = "argument"


def greet(greeting):
    print(greeting)

greet("Hello!")


def values(par1, par2):
    print(par1)
    print(par2)

values("1", "2")
    

# Multiple Parameters are utilized in through the first argument to first providing an initial value then it goes down to the 2nd parameter

def pets(canine, feline):
    print(canine)
    print(feline)

pets('dog', 'cat')

# Arguments can be anything that has outputs or values!
# Put variables inside of values?

value = int(input("give me a number!"))
value2 = int(input("give me a number!"))

def addition(value, value2):
    print(value)
    print(value2)
    total = value + value2
    print(total)

addition(value, value2)


