#list
shailu=["shailaja","sreekar","kiran","jatothu","shailu"]
print(shailu)
print(len(shailu))
print(type(shailu))
print(shailu[1:])
print(shailu[-2])

#append
shailu=["shailaja","sreekar","kiran","jatothu","shailu"]
shailu.append("jatothu")
print(shailu)

#insert
shailu=["shailaja","sreekar","kiran","jatothu","shailu"]
shailu.insert(1,"kamala")
print(shailu)

#extend
shailu=["shailaja","sreekar","kiran","jatothu","shailu"]
shailaja=["mounika","srikanth"]
shailu.extend(shailaja)
print(shailu)

#remove
shailu=["shailaja","sreekar","kiran","jatothu","shailu"]
shailu.remove("sreekar")
print(shailu)

#pop
shailu=["shailaja","sreekar","kiran","jatothu","shailu"]
shailu.pop(1)
print(shailu)

shailu=["shailaja","sreekar","kiran","jatothu","shailu"]
shailu.pop()
print(shailu)

#sort
shailu=["shailaja","sreekar","kiran","jatothu","shailu"]
shailu.sort()
print(shailu)

#count
shailu=["shailaja","sreekar","kiran","jatothu","shailu","shailaja"]
print(shailu.count("shailaja"))

#clear
shailu=["shailaja","sreekar","kiran","jatothu","shailu","shailaja"]
shailu.clear()
print(shailu)

#copy
shailu=["shailaja","sreekar","kiran","jatothu","shailu","shailaja"]
amma=shailu.copy()
print(amma)

#index
shailu=["shailaja","sreekar","kiran","jatothu","shailu","shailaja"]
print(shailu.index("kiran"))
#reverse
shailu=["shailaja","sreekar","kiran","jatothu","shailu"]
shailu.reverse()
print(shailu)
#Tuple
tuple1=("shailaja","sreekar","kiran","jatothu")
print(type(tuple1))
print(tuple1)

tuple = ("Shailaja","Jatothu","Sreekar")
y = ("Kiran",)
tuple += y
print(tuple)

result=(2,1,1,4,6)
a=result.count(1)
print(a)

result=(2,1,1,4,6)
a=result.index(1)
print(a)