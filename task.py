a=10
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)


a=10
b=15
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
print(a==b)
print(a!=b)


a=5
b=3
result=a>b and b>a
print(result)
result =a>b or a<b
print(result)
result=not(a>b)
print(result)


total=10
print(total)
total+=10
print(total)
total-=10
print(total)
total*=10
print(total)
total/=10
print(total)

#Bitwise
a=10  #1010
b=15  #1111
result=a&b   #1010
print(result)
result=a|b
print(result)
result=a^b
print(result)
result=~b
print(result)
result=a<<2
print(result)
result=a>>2
print(result)


my_list=[1,2,3.4,5,9]
print(3.4 in my_list)
print(4 in my_list)
print(3.4  not in my_list)
list1=[1,2,3,4]
list2=[2,3,4,5]
print(list1 is list2)
print(list1 is not list2)