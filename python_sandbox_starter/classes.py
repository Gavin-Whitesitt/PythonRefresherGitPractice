# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

#Create class
class User:
    #Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1
# Init user object
gavin = User('Gavin Whitesitt','gwhitesitt@gmail.com', 24)

print(type(gavin.age))

print(gavin.greeting())

gavin.has_birthday()
print(gavin.greeting())

#Extend class
class Customer(User):
#Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}, and my balance is {self.balance}'


#Init customer object
janet = Customer('Janet Johnson','janet@dumdumbish.com', 28)
janet.set_balance(500)

print(janet.greeting())


import json

items = json.loads('[{"id":1}]')

def greet(greeting, name):
    """Returns a greeting

    Args:
        greeting (string): A greet word
        name (string): A persons name

    Returns:
        string: A greeting with a name
    """
    return f'{greeting} {name}'