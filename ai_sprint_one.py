# If operand x is truthy returns operand x
x = 5
y = 100
print(x or y)

# If operand x is falsey returns operand y
x = 0
print(x or y)

# If operand x is falsey returns operand x
x = 0
y = 100
print(x and y)

# If operand x is truthy returns operand y
x = 50
print(x and y)

# If operand x is falsey returns True, else returns False
print(not x)