#global variable
global_var = 20

def my_function():
    print("global variable:", global_var)

my_function()
print("Global variable:", global_var)

#local variable
def my_function():
    local_var = 20
    print("local variable:", local_var)
my_function()

#modification of global
global_var = 20
def modify_global():
    global global_var
    global_var = 30
    print("Modified global variable:", global_var)
modify_global()
print("Global variable after modification:", global_var)



# variables.py
def func2():
    return "Function 2 from module2"