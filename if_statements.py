# conditional statements are used to execute code only under certain conditions

# Simple if statement
biscuits = 17
if biscuits >= 5:
    print("It's time for tea!")

# Nested if statements
rainbow = "red, orange, yellow, green, blue, indigo, violet"
warm_colors = "red, yellow, orange"
my_color = "orange"

if my_color in rainbow:
    print("Wow, your color is in the rainbow!")
    if my_color in warm_colors:
        print("Oh, by the way, it's a warm color.")