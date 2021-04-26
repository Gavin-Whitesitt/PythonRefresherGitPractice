# A List is a collection which is ordered and changeable. Allows duplicate members.

#Create list
numbers = [1,2,3,4,5]
fruits = ['Apples','Oranges','Grapes','Pears']

#Use constructor
numbers2 = list((1,2,3,4,5))

print(numbers, numbers2)

#Get a value: zero indexed
print(fruits[1])

#get length of list
print(len(fruits))

# Append (add to the end of the list)

fruits.append('Mangos')

#Remove from list
fruits.remove('Grapes')

#Insert into position
fruits.insert(2, 'Strawberries')

#Remove from position using pop
fruits.pop(2)

#Reverse list
fruits.reverse()

#add
fruits.append('Kiwis')

#Sort list alphabetically by default
fruits.sort()

#Reverse sort
fruits.sort(reverse=True)

#Change value

fruits[2] = 'Beets'
