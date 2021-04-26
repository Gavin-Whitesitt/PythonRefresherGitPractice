# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

print(person, type(person))

#use constuctor

person2 = dict(first_name='Sara', last_name='Williams')

#Get value
print(person['first_name'])
print(person.get('last_name'))

#Add key/value
person['phone'] = '555-555-5555'

#Get dict keys
print(person.keys())

#Get dict items
print(person.items)

#Copy dict
person3 = person.copy()
person3['city'] = 'Boston'

print(person3)

#Remove item
del(person['age'])
person.pop('phone')

#Clear
person.clear()

#Get length
print(len(person2))
