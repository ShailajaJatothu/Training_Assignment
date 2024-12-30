name="Shailaja"
print(len(name))
#max
name="Shailaja"
print(max(name))
#min
name="Shailaja"
print(min(name))
#single quotes
name='my name is shailaja'
print(name)
#double quotes
name="my name is shailaja"
print(name)
#triple quotes
name='''my self shailaja
I graduated from Cbit 
in the stream of IT'''
print(name)

#double quotes inside single quotes
name="my name is 'shailaja'"
print(name)
#•Slicing strings
name="Shailaja"
print(name[:])
name="Shailaja"
print(name[2:])
name="Shailaja"
print(name[:3])
name="Shailaja"
print(name[:-2])
name="Shailaja"
print(name[-2:])
name="Shailaja"
print(name[2:5])
name="Shailaja"
print(name[5:2])
#upper
name="Shailaja"
print(name.upper())
#lower
name="Shailaja"
print(name.lower())
#capitalize
name="shailaja"
print(name.capitalize())
#title
name="shailaja"
print(name.title())
#swapcase
name="Shailaja"
print(name.swapcase())
#find
name='''my self shailaja
I graduated from Cbit 
in the stream of IT'''
print(name.find("in"))
#index
name='''my self shailaja
I graduated from Cbit 
in the stream of IT'''
print(name.index("n"))
#replace
name="my self shailaja I graduated from Cbit "
print(name.replace("shailaja","shailu"))
#split
name="my self shailaja"
print(name.split(","))
print(name.split("a"))
#split
a="   shailaja   "
print(a.strip())
#isalpha
a="   shailaja   "
print(a.isalpha())
#isalnum
a="   shailaja   "
print(a.isalnum())

name="shailaja","jatothu"
a=" ".join(name)
print(a)