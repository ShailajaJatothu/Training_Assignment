#even number
a=int(input("enter a number"))
    if a%2==0:
        print("it is an even number",a)
    else:
        print("not a even number",a)

#factorial   5!=5*4*3*2*1
a=int(input("enter a number"))
fact=1
for i in range(1,a+1):
    fact=fact*i
print("factorial",fact)

#fibonacci           0 1 1 2 3 5 8
n=int(input("enter a number"))
a=0
b=1
for i in range(n):
  c=a+b
  a=b
  b=c
print(f"The {n}th Fibonacci number is: {a}")
print("c is",c)

#palindrome    aba
str=input("enter a string")
if(str==str[::-1]):
    print("palidrome",str)
else:
    print("it not palindrome")

#reverse
string=input("enter a string:")
print("Reversed string:",string[::-1])

#gcd of numbers
import math
a=int(input("enter a number"))
b=int(input("enter a number"))
print("GCD:", math.gcd(a, b))

#sum of Digits    123=6
num=int(input("enter a number"))
sum=0
while num>0:
    digit=num%10
    sum=sum+digit
    num=num//10
print("sum",sum)

#leap
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

#largest of 3 numbers
a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
print("largest of numbers is ",max(a,b,c))

a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
if(a>b):
  if(a>c):
    print("a is greater")
  else:
    print("c is greater")
else:
  if(b>c):
    print("b is greater")
  else:
    print("c is greater")

#Multiplication Table 2*1=2   2*2=4    2*3=6
num=int(input("enter a number"))
for i in range(1,11):
    print("multiplication of the numbers",num*i)

#fah to celsius
fah=float(input("enter a temperature"))
cel=5/9*(fah-32)
print("celsius in temperature",cel)

#number of digits
num=int(input("enter a number"))
print("number of digits",len(str(num)))

#anagrams
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if sorted(str1) == sorted(str2):
    print("Anagrams")
else:
    print("Not anagrams")

#bubble sort
lst = [1,2,7,4,3,9]
for i in range(len(lst)):
    for j in range(len(lst)-i-1):
        if lst[j]>lst[j+1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
print("Sorted list:", lst)

#armstrong   123=(1) *power+(2)*power+(3)*power=num
num=int(input("enter a number"))
n=len(str(num))
original = num
sum = 0
while num > 0:
    digit = num % 10
    sum += digit**n
    num //= 10
if original== sum:
    print(f"{original} is an Armstrong number.")
else:
    print(f"{original} is not an Armstrong number")

#perfect number  6=1+2+3
n=int(input("enter a number"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum==n:
    print("perfect number",n)
else:
    print("not perfect number",n)

#Swap Two Numbers
a=10
b=12
print("before swapping",a,b)
a=a+b
b=a-b
a=a-b
print("after swapping ",a,b)


a=10
b=12
print("before swapping",a,b)
a=a*b
b=a//b
a=a//b
print("after swapping ",a,b)

a=10
b=12
print("before swapping",a,b)
c=a
a=b
b=c
print("after swapping ",a,b)

#Sum of Natural Numbers
n = int(input("Enter a number "))
if n < 0:
    print("enter a positive integer.")
else:
    sum_of_numbers = n * (n + 1) // 2
    print("sum of the first natural numbers",sum_of_numbers)

#Count Vowels in a String
n = input("Enter a string: ")
count = 0
for i in n:
    if i in "aeiouAEIOU":
        count=count+1
print("No of vowels in the string:", count)

#number pattern
for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()

# *
# *  *
# *   *  *
# *   *   *  *
for i in range(0,5):
        for j in range(1,i+1):
            print("*", end=" ")
        print()

# 1
# 2 2
# 3 3 3
# 4 4 4 4
for i in range(1,5):
        for j in range(1,i+1):
            print(i,end=" ")
        print()

# 1
# 1   2
# 1   2    3
# 1   2    3   4

for i in range(1,5):
        for j in range(1,i+1):
            print(j,end=" ")
        print()

#Area of a Circle 3.14*r^2
radius=float(input("enter radius"))
radius=3.14*(radius**2)
print("radius of circle",radius)

#area of rectangle  1/2*l*b
length=float(input("enter a length of rectangle"))
breadth=float(input("enter breadth of rectangle"))
area=0.5*length*breadth
print("area of rectangle",area)

#prime number
num = int(input("Enter a number "))
count= 0
for i in range(2,num):
  if num%i==0:
    count =count+1
    break
if count == 0:
  print('Prime')
else:
    print("not prime")

#hcf
num1 = int(input("Enter a number "))
num2 = int(input("Enter a number "))
while num2:
    num1,num2=num2,num1%num2
print("hcf",num1)

#lcm
a = int(input("Enter a number "))
b = int(input("Enter a number "))
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
lcm=abs(a*b)//gcd(a,b)
print("lcm of 2 numbers is",lcm)

#Count consonants in a String
n = input("Enter a string: ")
count = 0
for i in n:
    if i not in "aeiouAEIOU":
        count=count+1
print("No of consonants in the string:", count)

#count no of vowels and consonants
n=input("enter a string")
vowels_count=0
consonants_Count=0
for i in n:
    if i  in 'aeiouAEIOU':
        vowels_count=vowels_count+1
    else:
        consonants_Count=consonants_Count+1
print("consonants_Count",consonants_Count)
print("vowels_count",vowels_count)

#Second Smallest and Second Largest Element in a list
list=[2,4,7,1,9,3]
list.sort()
print("second smallest element is",list[1])
print("second largest element is",list[-2])

#Remove duplicates from a list.
list1=[1,2,3,5,1,2]
print(list(set(list1)))

list1=[1,2,4,5,3,5,3,1]
unique_list=[]
   for i in list1:
       if i not in unique_list:
           unique_list.append(i)
print("unique list is",unique_list)

#Basic Calculator:
a=float(input("enter a number"))
b=float(input("enter a number"))
operator=input("enter the operator you want to perform operation")
if operator == '+':
    print(a+b)
elif operator == '-':
    print(a-b)
elif operator == '*':
    print(a*b)
elif operator == '/':
    print(a/b)
else:
    print("invaid operator")
#Count digits in a number   12345=5
num=int(input("enter a number"))
count=0
while num>0:
    count=count+1
    num=num//10
print("Count digits in a number is",count)

#Print all Divisors of a given Number
num=int(input("enter a number"))
for i in range(1,num+1):
    if num%i==0:
        print("Divisors of a number 36 is",i)

#selection sort
array=[1,35,7,3,9,23,64]
for i in range(len(array)):
    if array[i]>array[i+1]:
        array[i],array[i+1]=array[i+1],array[i]
    print("the sorted array is",array)

list