import math
print("square root of a number",math.sqrt(25))

import random
print(random.randint(1,100))

import datetime
today = datetime.date.today()
print(today)

# modules.py
def greet(name):
    return f"Hello, {name}"

def add(a, b):
    return a + b
# main.py
import modules

print(modules.greet("Shailaja"))
print(modules.add(5, 10))

# module1.py
def func1():
    return "Function 1 from module1"



# main.py
from package import modules, variables

print(modules.func1())
print(variables.func2())

