# If/ Else conditions are used to decide to do something based on something being true or false

x = 9
y = 10

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

#Simple if 
if x > y:
    print(f'{x} is greater than {y}')

#If/else
if x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{y} is greater than or equal to {x}')


#elif
if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{y} is greater than {x}')

#Nested if
if x > 2:
    if x <= 10:
        print(f'{x} is greater than 2 and less than or equal to 10')

# Logical operators (and, or, not) - Used to combine conditional statements

if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')

#not
if not(x == y):
    print(f'{x} is not equal to {y}')


# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object
x = 4

numbers = [1,2,3,4,5]

if x in numbers:
    print('x is in numbers')

#not in

if y not in numbers:
    print('y is not in numbers')

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

#is
x=1
y=1

if x is y:
    print('x is y')