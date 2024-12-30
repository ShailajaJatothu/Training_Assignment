
#Arithmetic Operators
a=10
b=15
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)

#Logical Operators
a=10
b=20
c=30
result=(a>b) and (b>c)
print(result)
result=(a>b) or (a<c)
print(result)
result=not(a>b)
print(result)

#Bitwise operators
a=8  #1000
b=6   #110
c=a&b
print(c)
c=a|b
print(c)
c=~b
print(c)
c=b<<2
print(c)
c=b>>2
print(c)
c=a^b
print(c)

#Assignment Operators
a=20
a+=10
print(a)
a-=10
print(a)
a*=10
print(a)
a%=10
print(a)
a/=10
print(a)
a//=10
print(a)

#Membership Operator
list1=[1,2,3,4.5,8,9]
print(4 in list1)
print(4 not in list1)
print(2 in list1)
print(2 not in list1)

#Identity Operators
list=[1,2,4,5,7]
list1=[1,3,4,6,7]
print(list is list1)
print(list is not list1)

a=10
b=10
print(a is b)
print(a is not b)

#comparison operators
a=21
b=34
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)