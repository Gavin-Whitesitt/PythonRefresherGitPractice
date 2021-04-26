# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
#Creat tuple
fruits = ('Apples', 'Oranges', 'Grapes')
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

fruits2 = ('Apples')

#define with trailing comma or it will be read as string
print(fruits2, type(fruits2))

#see trailing comma
fruits3 = ('Apples',)

print(fruits3, type(fruits3))

print(fruits[1])

#cant change value:
#fruits[0] = 'Pears'

#Delete tuple
del fruits2, fruits3

#get length
print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.

#Create set 
fruits_set = {'Apples', 'Oranges', 'Mango'}

#Check if in set
print('Apples' in fruits_set)

#Add to set
fruits_set.add('Grape')

#Remove from set
fruits_set.remove('Grape')

#Clear set
fruits_set.clear()

#del fruits_set

print(fruits_set)