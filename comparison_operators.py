# These are the 10 comparison operators, they all return a bool value
# < strictly less
print(7 < 5)
# <= less than or equal
print(4 <= 5)
# > strictly greater than
print(7 > 5)
# >= greater than or equal
print(7 >= 5)
# == equal
print(7 == 7)
# != not equal
print("tongue" != "dog")

# Any expression that returns an integer is a valid comparison operand
print(5 == 3 + 2)

# since comparison operators return bool values you can join them using logical operators
x = -5
y = 10
z = 12
print(x < y and y <= z)

# There's also comparison chaining for more complex comparisons
print(x < y <= z)
#is equivalent to joining, except y is only evaluated once:
print(x < y and y <= z)
# Tools for code quality generally recommend chaining over joining


# is object identity
# is not negated object identity
#
# in membership
#
# not in negated membership.