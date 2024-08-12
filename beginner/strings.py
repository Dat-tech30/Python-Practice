# String variables are values that are represented as words, characters, and even numbers that are enclosed in quotation marks " " / ' '
# For example variables of x or toy in this case can be represented as marble

toy = "marble"

print(toy)

# Escape Characters are special syntax used for strings if you need to use the single quote ' since using a single quote conflicts with prexisting quotation defining a variable 
# backslash ex. \
# backslash n creates a new line ex. \n

sentence = "How\'s it going? Anything exciting happened?"

print(sentence)

new_sentence = "I went to the icecream store and there were a variety of options and so many different types of flavors. \n that I chose 3 different types of flavors; chocolate, vanilla, and mint chip!"

print(new_sentence)

# Multiline strings are used if the strings are stretched over and are very long using 3 quotation marks """ """

toy = """A toy or plaything is an object that is used primarily to provide entertainment. Simple examples include toy blocks, board games, and dolls. Toys are often designed for use by children, although many are designed specifically for adults and pets."""

print(toy)

# String Concatenation is adding a string variable to another string
# add a plus + after the you print

hobby = "music"

print("I love " + hobby)

# F string is used more if you need to add more variables and also is easier syntax
# Type and F/f before the string. Put the variable names in curly brackets {}

hobby = "video games"
hobby_length = "3 years"
favorite_game = "Minecraft"

story = F"""My hobby is that I love to play {hobby} and I have been playing for {hobby_length} and out of those {hobby_length} my favorite game is {favorite_game}!"""

print(story)

# R Strings is the same as F strings however adding in escape characters for reference!

cat = r""" _._     _,-'""`-._
(,-.`._,'(       |\`-/|
    `-.-' \ )-`( , o o)
          `-    \`_`"'-"""

print(cat)
