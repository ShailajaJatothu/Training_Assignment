
print("hello")

#1.Numeric
a=10
b=12.3
d=123e3
c=1+2j
print(a,b,c)
print(type(a))
print(type(b))
print(type(c))
print(d)

#type implicit conversion
a=10
b=2.3
result=a+b
print(result)
print(type(result))

#explicit
a=10
print(type(str(a)))
print(float(a))

#string
str="shailaja"
print(str)
print(type(str))
print(str[0])

#List
list=[1,2.3,1+2j,"shailaja"]
print(list)
print(list[2:])
print(type(str))
list[0]="hi"
print(list)

#Tuple
tuple=(1,2,3,4.3,3+2j)
print(tuple)
print(type(tuple))
print(tuple[-1])
print(tuple+tuple)
print(tuple*3)

tuple[2]="hi"

#Range
for i in range(5):
  print(i)

#Dictionary
dict={1:"shailaja",2:"sreekar",3:"kiran"}
print(dict)
print(type(dict))
print(dict.keys())

print(dict.values())

#Boolean
print(type(True))

a = 10
b = 20
result = a < b
print(result)

print(type(true))

print(type("False"))

# Create a set
mset = {1, 2, 3, 4, 5}
print(mset)

mset.add(6)
print(mset)

fs = frozenset([1, 2, 3, 4])
print(fs)

print(type(fs))

fs = frozenset([1, 2, 3, 4])
print(fs)
fs.add(5)

fs = frozenset([1, 2, 3])
print(2 in fs)
print(5 in fs)

#Byte
b_data = b"hello"
print(type(b_data))

#Memory view
b_data = b"shailaja"

# Create a memoryview
mv = memoryview(b_data)

# Access the first element
print(mv[0])

#Byte array
ba = bytearray(b"shailaja")
ba[0] = 74
print(ba)

#None
def my_function():
    pass
result = my_function()
print(result)

if not None:
    print("None is False")  # Output: None is False

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

person1 = Person("shailaja", 21)
person1.display_info()

from enum import Enum

class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

# Accessing enum members

print(Day.MONDAY.value)
for day in Day:
    print(day.name, day.value)

def square(num):
    return num ** 2

print(square(5))

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) >   0:
            return self.stack.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return "Stack is empty"


s = Stack()
s.push(10)
s.push(20)
print(s.pop())
print(s.peek())


def my_function():
    pass
result = my_function()
print(result)  # Output: None

if not None:
    print("None is False")  # Output: None is False
    a = 10
    b = 20
    result = a < b
    print(result)  # True