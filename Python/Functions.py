def my_func(param1='default'):
	print("my first python function!")


my_func()




def hello():
	return ("hello")


result=hello()
print(result)


def addNum(num1,num2):
	return num1+num2

result=addNum("2","3")
print(result)



#Filter function

mylist=[1,2,3,4,5,6,7,8]

def even_bool(num):
	return num%2==0

evens=filter(even_bool,mylist)


 #lambda expression
lambda num:num%2==0

evens=filter(lambda num:num%2==0,mylist)
print(list(evens))


# string
st="hello"
st.lower()
st.upper()
st.split()

tweet="Go Sports!#Sports"

print(tweet.split("#"))

# In operator
