from array import *;

# arr=array('i',[45,5,6,9,8,7,4,5,6,3,10,15])

# for ele in arr:
#     print(ele,end=" ")
# print(type(arr))

# arr.append(50)
# arr.append(100)
# print(arr)
# print(arr.buffer_info())
# print(len(arr))
# # arr.clear() # delete all element in array
# print(arr)

size=int(input("Enter a size of array: "))
print("Enter a Values : ")
arr=array('i',[])

for i in range(0,size):
    x=int(input())
    arr.append(x)
print(arr)

val=int(input("Enter a value you want to search: "))
idx=int(0)
for ele in arr:
    if(ele==val):
        print(f"{val} is present in the array at index: {idx}")
        break
    idx+=1
else:
    print(f"{val} is not present in the array .")
    

