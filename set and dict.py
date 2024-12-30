result={1,2,5,9,3,4}
print(result)
#type
print(type(result))
#Add()
result={1,2,5,9,3,4}
result.add(8)
print(result)

#Difference()
set1={1,2,3,4}
set2={2,5,7,9}
print(set1.difference(set2))

#update
set1={1,2,3,4}
set2={2,5,7,9}
set1.update(set2)
print(set1)
#clear
set1 = {1, 2, 3, 4}
set1.clear()
print(set)  # Output: set() (an empty set)

#difference_update
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6}
set1.difference_update(set2)
print(set1)

#discard
set1 = {1, 2, 3, 4}
set1.discard(3)
print(set1)
set1.discard(5)
print(set1)
#intersection_update
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.intersection_update(set2)
print(set1)

#isdisjoint
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2))
set3 = {3, 7, 8}
print(set1.isdisjoint(set3))

#issubset
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print(set1.issubset(set2))
set3 = {6, 7}
print(set3.issubset(set2))

#update
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2)
print(set1)

#all
set1 = {1, 2, 3}
set2 = {1, 0, 3}
print(all(set1))
print(all(set2))
#any
set1 = {1, 2, 3}
set2 = {0, 0, 0}
print(any(set1))
print(any(set2))
print(any({}))


# Intersection():return intersection of two sets as a new set.
set1={1,2,3,4}
set2={2,5,7,9}
print(set1.intersection(set2))
# Isdisjoin():return true if two set have null intersection.
set1={1,2,3,4}
set2={2,5,7,9}
print(set1.isjoint(set2))
# Issubset():return true if another  set contains this set.

# Pop():it remove the element which placed as 1st element.
set2={2,5,7,9}
print(set1.pop())
# Remove():it remove a specific element from the set if the element is not available it raises an exception key error.
set1={1,2,3,4}
set1.remove(3)
print(set1)
# Symmetric_difference():return the symmetric difference of two sets as a new set.
set1={1,2,3,4}
set2={2,5,7,9}
print(set1.symmetric_difference(set2))
# Union():it will combine set one or more set and it will return the unique element.
set1={1,2,3,4}
set2={2,5,7,9}
print(set1.union(set2))
# Update():update a set  with the union of itself and others
set1={1,2,3,4}
set2={2,5,7,9}
set1.update(set2)
print(set1)
# Len():return the length of set.
set2={2,5,7,9}
print(len(set2))
# max():return largest element in the set.
set2={2,5,7,9}
print(max(set2))
# sorted():it return new sorted element in set.
set2={2,5,1,3,9}
print(sorted(set2))

#Dictionary
result={1:"shailaja",2:"sreekar",3:"kiran",4:"jatothu"}
print(result)

#get method
result={1:"shailaja",2:"sreekar",3:"kiran",4:"jatothu"}

print(result.get(2))

#values
result={1:"shailaja",2:"sreekar",3:"kiran",4:"jatothu"}
print(result.values())
#keys
result={1:"shailaja",2:"sreekar",3:"kiran",4:"jatothu"}
print(result.keys())

#pop
result={1:"shailaja",2:"sreekar",3:"kiran",4:"jatothu"}
print(result.pop(2))

#update
result={1:"shailaja",2:"sreekar",3:"kiran",4:"jatothu"}
result.update({2:"jatothu"})
print(result)

#popitem
result={1:"shailaja",2:"sreekar",3:"kiran",4:"jatothu"}
result.popitem()
print(result)

#item
result={1:"shailaja",2:"sreekar",3:"kiran",4:"jatothu"}
result.items()
print(result)

#clear()
result={1:"shailaja",2:"sreekar",3:"kiran",4:"jatothu"}
result.clear()
print(result)