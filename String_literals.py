# You can escape so that python interprets the next character as a part of the string using the \
print('You\'re so right, aren\'t you?')

# Multi-line strings:
print("""
This 
is 
a 
multi
line
string.
""")

# You can use variables in strings using format strings:
name = "Enki"
# This is the modern syntax f-strings
print(f"Hi, {name}!")

# You can also use f-strings to round numbers to a certain decimal place:
number = 2.9878
print(f"The number is: {number:.2f}")

# You can use the % operator, this comes from C language. It needs a formatter specifier that acts
# as a variable. You then specify the arguments outside the string:
print("Hi, %s!" % name)

# You can also use the old C format syntax to control the number of decimals in a digit string
print(11/3)
print("%.3f" % (11/3))
print("%.2f" % (11/3))

# Lastly there's str.format()
name = "Enki"
age = 26
print("Hi, my name is {}, I'm {} years old".format(name, age))

# You can specify the order and amount of times values in the format function are inserted:
print("Hi, my name is {1}, I'm {0} years old".format(name, age))
print("Hi, {0}, I'm {0} years old".format(name, age))

# You can also use keys inside placeholders:
print("The {movie} movie at {theatre} was {adjective}!".format(movie="Star Wars", adjective="incredible", theatre="IMAX"))

