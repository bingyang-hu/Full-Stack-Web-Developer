if 1<2:
	print('yes!')





# For loops


#1.Iterate through a list
seq=[1,2,3,4,5,6]

for item in seq:
	print(item)


#2. Iterate through a dic

d={"Sam":1,"Frank":2,"Dan":3}

for k in d:
	print (d[k])


#3.Iterate through a list of tuple

mypairs=[(1,2),(3,4),(5,6)]

#Unpacking tuple in for loop

for (tup1,tup2) in mypairs:
	print(tup2)
	print(tup1)


# while loop

i=1

while (i<5):
	print (i)
	i=i+1;



# Range function

list(range(0,5))

#List Comprenhension

x=[1,2,3,4]
out=[]
for num in x:
	out.append(num**2)
print(out)


out2=[num**2 for num in x]

print(out2)






