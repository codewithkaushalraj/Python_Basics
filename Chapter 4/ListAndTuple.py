
list=["kaushal",45,45,334,"Math","coding",{
    "name":"kaushal"
      }]
print(list)
print(list[6])
list[1]="raj";
print(list)
list.append("Money")
print(list)

l1=[12,43,64,3,2,44,25,10];
l1.sort();
l1.reverse()
print(l1)
l1.insert(3,"Love") # means at third index add "Love"
print(l1)

print(l1.pop(4))  # delete the element at indx and in return they will gave the value that are present at these index
print(l1)

l1.remove(2) # remove the element 2 from the list
print(l1)


tuple=(44,12,23,44,567,44,"KAUSHAL","RAJ");
print(tuple)
print(type(tuple))

# if you want to one element in the tuple only
t2=(23,)
print(t2)
print(type(t2))

print(tuple.count(44))  # it will count the occurances of tuple