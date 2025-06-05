# all the dope imports
import random, numpy, pandas

# doing all the basic things using python

#normal array
e = [1, 2, 3] # dint have to define the size. the arrays are more like ArrayLists

# defining variables of every data type
x = 5
y = 2.2
x, y ,z = 1 ,2 ,3 # you can define multiple variables on the same line
bob, dob, lob = 1, "cat", 2.2 # they dont have to be the same data type
lit, bit, kit = "money" # can assign multiple variables the same value at once

# "unpacking" / breaking a list into individual variables
candy = ["bean", " worm", "apple"]
h, i, j = candy # these variables now hold the values that were in the tuple

#type casting
a = 1
str(a)
int(a)
float(a)
print(type(a)) # prints the data type

#generate a random number
print(random.randrange(0,1000))# prints a random number between 0 and 1000

# printing the nth position of a string
a = "doggy dog world"
print(a[2]) # prints "g"

#reading user input
user_input = input("prompt for user input + scanner + variable storage in one line") # mad easy to do user input in python
#writing to the screen
print("this is mad easy" + str(x)+ str(x*y)) # concatonate uses '+' or ','
print("too east ngl", str(5))

#if statment
if x < 5:
    print("damn")
zillow = "boulderdash"
if("dash" in zillow ):
    print("gay")
#if else statement
if("asS" in zillow):
    print("yaga")
elif("dosh" in zillow):
    print("boogie")
else:
    print("else")


#for loop
s = "crappy"
for i in range(0,len(s)): # need to range to set initial iterator value and where it stops, len is the length function
    print(i)
#check if a string contains a certain string / number / character
print("ap" in x) # uses the 'in' keyword
# while loop

#switch-case block
match x:  # only available in python 3.10+ , otherwise you have to use a if-elif-else chain
    case 1:
        print("blood")
    case 2:
        print("gud")
    case 3:
        print('hub')
    case _:
        print('default')

#try - except block
try:
    print(x)
except ExceptionType:
    #code to execute if the error occurs
except OtherExceptionType:
    # you can do this mutiple times with different exception types


# defining a method / function
def functionName(arguments): # just take the paramters as generic data types that get defined by the user through usage or through the data being passed in during run time
    return "candy" # theres no access modifiers in defining a function
functionName(x) # to use the function, its about the samee as when you use it in java

#arraylist
list = [] # litterally just use the normal list here since its essentially an ArrayList ( fuck memory efficiency ig)
list.append(5)

#linkedlist
#none built in, youd have to make it yourself. just use dequq for the same purposes if you need to

#queue
from collections import deque
stack = deque()
stack.append(1)
stack.pop()

#stack
#just use deque

#threading
from threading import Thread # how to use threading in python
def function(): # you define a function/ block of code you want to implement
    print("running")
t = Thread(target = function) # then the target function is pointed to for the new thread
t.start() # executes the new thread


