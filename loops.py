
#Loops
for i in range(1,10):
  print(i)

#List
list=["shailaja","sreekar","kiran"]
for i in list:
  print(i)

#Tuple
a=(1,2,34,3.4)
for i in a:
  print(i)

for i in range(1,12,2):
  print(i)

for i in range(12,1,-2):
  print(i)

for i in range(20):
  if i%2==0:
    print(i)

for i in range(1,3):
  for j in range(1,3):
      print(i*j)

i=1
while(i<=5):
  i=i+1
  print(i)


i=5
while(i>1):
  i=i-1
  print(i)

i = 1
while True:
    print(i)
    if i == 5:
        break
    i += 1

i = 0
while i < 10:
    i += 1
    if i == 3:  # Skip when i is 3
        continue
    print(i)

i=1
while(i<3):
  print(i)
  i=i+1
  j=1
  while(j<3):
    print(j)
    j=j+1

