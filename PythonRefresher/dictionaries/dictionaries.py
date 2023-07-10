"""
Dictionaries
"""

user_dictionary = {
    'username': "robhitt",
    'name': 'Rob',
    'age': 45,
}

print(user_dictionary.get("username"))
print(user_dictionary["username"])
user_dictionary["married"] = False
print(user_dictionary)

user_dictionary.pop("age")  # remove item from dictionary
print(user_dictionary)

# user_dictionary.clear()  # remove all info

# del user_dictionary  # remove entire dictionary

# PROPERTIES OF DICTIONARY
for x in user_dictionary:
    print(x)

# VALUES OF DICTIONARY
for x, y in user_dictionary.items():
    print(y)

# COPY DICTIONARY
user_dictionary2 = user_dictionary.copy()

# ASSIGNMENT
my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}

for x, y in my_vehicle.items():
    print(x, y)

vehicle2 = my_vehicle.copy()

vehicle2["number_of_tires"] = 4

vehicle2.pop("mileage")
print(vehicle2)
