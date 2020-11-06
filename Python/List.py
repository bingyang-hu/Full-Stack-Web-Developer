


#1. To add something

#.append vs .extend

mylist1=['a','b','c','d','e']

mylist1.append(['x','y','z'])

print(mylist1)


mylist2=['a','b','c','d','e']

mylist2.extend(['x','y','z'])

print(mylist2)

#2. To remove something

# .pop will return a element, and if it's empty, then the last one will be removed.

item=mylist1.pop()

print(item)

print(mylist1)

# You can choose to remove any one from the list using index:

item1=mylist2.pop(2)

print(item1)
print(mylist2)



#3. To sort

mylist3=[2,5,3,1,6,0,3]

mylist3.reverse()

print(mylist3)

mylist3.sort()

print(mylist3)
