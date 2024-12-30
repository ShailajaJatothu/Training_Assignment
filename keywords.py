#1.and
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
#2.or
a=12
b=18
c=a>b or a>c
print(c)

#3.not
a=12
b=18
c=not(a>b)
print(c)

#4.if
age=int(input("enter a number"))
if(age>18):
  print("you are eligible for voting")

#5.else
age=int(input("enter a number"))
if(age>=18):
  print("you are eligible for voting")
else:
  print("you are not eligible for voting")

#6.elif
a=10
b=12
c=13
if(a>b)and(a>c):
  print("a is greater")
elif(b>c):
  print("b is greater")
else:
  print("c is greater")

#7.while
i=10
while(i<20):
  print(i)
  i=i+1

#8.for
for i in range(5):
  print(i)

#9.in
list1=[1,2,3,4,1,2]
print(12 in list1)
#10.try
a = 100
try:
    if a < 0:
        raise ValueError("The value of 'a' cannot be negative.")
    else:
        print("The value of 'a' is valid",a)
except ValueError as e:
    print(f"Error: {e}")

#11.except
a = -100
try:
    if a < 0:
        raise ValueError("The value of 'a' cannot be negative.")
    else:
        print("The value of 'a' is valid",a)
except ValueError as e:
    print(f"Error: {e}")

#12.finally
a = 100
try:
    if a < 0:
        raise ValueError("The value of 'a' cannot be negative.")
    else:
        print("The value of 'a' is valid",a)
except ValueError as e:
    print(f"Error: {e}")
finally:
  print("execution of try and except block is complted")

#13.def
def sum(num1,num2):
  return num1+num2
print(sum(12,13))

#14.Return
def sum(num1,num2):
  return num1+num2
print(sum(12,13))

#15.Import
import numpy as np
array=np.array([1,2,3,4,5])
print(array)

#16.Class
class Person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def display(self):
    print("name",self.name)
    print("age",self.age)
Person1=Person("Shailaja",21)
Person1.display()

#17.From
from math import sqrt
print(sqrt(25))

#18.As
import numpy as np
import pandas as pd

#19.True
is_raining = True
if is_raining:
    print("Take an umbrella!")

#20.False
is_raining = False
if is_raining:
    print("Take an umbrella!")


#21.None
a=90
if a is None:
  print("the value is none")
else:
  print("it is not none")

a=None
print(a)

#22.Is
a=10
b=20
print(a is b)

#23.Lambda
add = lambda x, y: x + y
result = add(5, 3)
print("The sum is:", result)

#24.With
file=open("example.txt","r")
content=file.read()
print(content)
file.close()

with open("example.txt", "r+") as file:
    file.truncate(0)
#25.Global
global_var = 20
def modify_global():
    global global_var
    global_var = 30
    print("Modified global variable:", global_var)
modify_global()
print("Global variable after modification:", global_var)
#26.Non-local
def outer_function():
    x = 10

    def inner_function():
        nonlocal x
        x += 1
        print("Inner x:", x)

    inner_function()
    print("Outer x:", x)

outer_function()







