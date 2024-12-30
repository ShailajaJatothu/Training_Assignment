
#If statement
a=int(input("enter a number"))
if(a>0):
  print("it is a positive number")

#if else statement
a=10
b=20
if(a>b):
    print("a is greater")
else:
  print("b is greater")

#if elif else statement
signal=str(input())
if(signal=="red"):
  print("stop")
elif(signal=="green"):
  print("go")
elif(signal=="yellow"):
  print("get ready")
else:
  print("invalid signal")

#nested if statements
a=21
b=43
c=12
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
#eligible for vote
age=int(input("enter a number"))
if(age>=18):
  print("you are eligible for vote")
else:
  print("you are not eligible for vote")
