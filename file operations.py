#list creation
list=[1,3,4.2,"shailaja",2+8j,"jatothu"]
print(list)

#access the items from the list
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[2:])
print(list[-2])

#replace
list[2]=5.4
print(list)

list[3]="sreekar jatothu"
print(list)

#append
list.append("kiran jatothu")
print(list)

#insert new items into the list
list.insert(3,"shailaja jatothu")
print(list)

#extend
list1=[1,4,7,10]
list.extend(list1)
print(list)

#remove
list.remove("shailaja jatothu")
print(list)
#clear
list.clear()
print(list)

#print name 100 times
# Take input from the user
name = input("Enter your name: ")
for i in range(100):
    print(name)

name = "shailaja"
result = " ".join([name] * 100)
print(result)

print(result)

name="Shailaja Jatothu"
for i in range(100):
    print(name)

#number is even or odd
num=int(input("enter a number"))
if num%2==0:
    print("it is even number",num)
else:
    print("it is odd number",num)
#print 7 th table
for i in range(1,11):
    print(f"7*{i}={7*i}")
#two variables comparison
num1=int(input("enter 1st number"))
num2=int(input("enter 2nd number "))
smallest=min(num1,num2)
largest=max(num1,num2)
print("min of number is",smallest)
print("max of number is",largest)
#largest of 3 numbers
a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
print("largest of numbers is ",max(a,b,c))


#file operations
file=open("example.txt","r")
content=file.read()
print(content)
file.close()

#write
file=open("example.txt","w")
content=file.write("python is very easy and easy to learn")
print(content)
file.close()

#append
file=open("example.txt","a")
content=file.write("I have graduated from cbit in the stream of information technology with an aggregate percentage of 85")
print(content)
file.close()

#whether file exists or not
import os
if os.path.exists("example.txt"):
    print("file exists")
else:
    print("file doesnot exist")

#readlines
file=open("example.txt","r")
content=file.readlines()
print(content)
file.close()


