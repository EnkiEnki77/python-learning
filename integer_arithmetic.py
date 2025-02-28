# To raise an integer to the power of something using the exponent operator
print(3**5)

# To evaluate the modulus of two numbers use the modulo operator
print(7%3)

# To convert a 24 hour time into 12 hour
def convert_time(hr):
    conversion = None
    if hr == 0:
        conversion = 12
    elif hr < 12:
        conversion = int(hr)
    else:
        conversion = int(hr % 12)
    return conversion

# hr = input('Enter time in military hours: ')
#
# print(convert_time(hr))

# Investment planning
money = 100
interest = .05
years = 10

def investment_value(x, r, y):
    return x *  ((1 + r)**y)

print(investment_value(money, interest, years))