# In set you can not no any appers more than one time all the element should be unique 
sets=set()  # this is use to create an empty sets
# set is an unordered collection of elements
print(sets, type(sets)) 

sets.add(45)
sets.add(1)
sets.add(95)
sets.add(33)
sets.add(45)

print(sets)
# sets.clear()  # used to clear the set
print(sets)

set2=sets.copy()  # It will create a shallow copy not deep copy
print(f"the elements of a copied set is : {set2}")  

set2.remove(45) # remove element 1 from set2
print(set2)

s1={2,3,4,5,6}
s2={4,6,12,34,5}

print(s1.union(s2))
print(s1.intersection(s2))

# Important Note : List ko hum set ke andar include hi nahi kar sakte