# Practice Review!
# This is an awesome comment!
'''
This is also an awesome comment!
'''

var1 = 21
var_1 = "21"

add1 = 1
add2 = 2
float1 = 222.10
float2 = 21.22
total =  add2 / add1

string = str(float1)
num1 = type(float1)

print("Hello World")
print(total)

print("Hey the number is " + string)
print(num1)

print(f'Here are some numbers that I am print right now {add1}, {add2}, and the last one! {total}')
print(r'''

╭━━━╮┈┈╱╲┈┈┈╱╲
┃╭━━╯┈┈▏▔▔▔▔▔▕
┃╰━━━━━▏╭▆┊╭▆▕
╰┫╯╯╯╯╯▏╰╯▼╰╯▕
┈┃╯╯╯╯╯▏╰━┻━╯▕
┈╰┓┏┳━┓┏┳┳━━━╯
┈┈┃┃┃┈┃┃┃┃┈┈┈┈
┈┈┗┻┛┈┗┛┗┛┈┈┈┈

''')


# functions
# parameters and arguments!

stuffed_animal = 12.99
animal_hat = 15.99

def animals(mammals, birds, fish):
    print(f'Welcome to the Zoo! Where are plenty of animals for you to see!')
    print(f'We have plenty of {mammals}, {birds}, {fish}')
    print('We also have a gift shop for you to explore!')
    user = input('Which animal would you like to see in order?')
    print(f'Great choice! We will go see the {user} first!')
    print("Buying the stuffed animal and hat? Great choice!")
    total = stuffed_animal + animal_hat
    print(f'total is gonna be ${total}')


animals("mammals", "birds", "fish")
