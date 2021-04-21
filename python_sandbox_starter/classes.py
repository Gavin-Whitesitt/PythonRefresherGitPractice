# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

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