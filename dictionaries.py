# The simplest way to create a dict is hardcoding it with all its key:value pairs
birds = {"pigeon": 12, "sparrow": 5, "red crossbill": 1}
prices = {'espresso': 5.0, 'americano': 8.0, 'latte': 10, 'pastry': 'various prices'}
empty_dict = {}

# print(type(empty_dict))
# print(type(birds))
# print(type(prices))

# You can also use the dict constructor
another_empty_dict = dict()
print(type(another_empty_dict))
another_birds_dict = dict(pigeon = 2, sparrw = 5, red_crossbill = 1)
print(type(another_birds_dict))
print(another_birds_dict)


# TO add key value pairs to a dict:

another_birds_dict['eagle'] = 4
print(another_birds_dict)

# To read the key of a dict:
print(another_birds_dict['eagle'])


my_pets = {'dog': {'name': 'Dolly', 'breed': 'collie'},
           'cat': {'name': 'Fluffy', 'breed': 'maine coon'}}

# To access keys in a nested dictionary:
print(my_pets['dog']['name'])


trilogy = {'IV': 'Star Wars', 'V': 'The Empire Strikes Back', 'VI': 'Return of the Jedi'}
print(trilogy['IV'])  # Star Wars

# To overwrite the value of a preexisting key use the same syntax you would for adding a new key/value pair
# but pass the preexisting key instead of a new one.
trilogy['IV'] = 'A New Hope'
print(trilogy['IV'])  # A New Hope