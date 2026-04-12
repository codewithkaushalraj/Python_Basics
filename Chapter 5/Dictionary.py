# In dictionary we will store the data in the form of key : value pairs

marks={
    "kaushal":80,
    "raj":89,
    "mohan":56,
    "rani":33
}
print(marks,type(marks))
print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"rani":45,"puja":99 })   # if keys match with the dictionary then they will update the value and if key not present in the dictionary then they will create a  new key value pair into the ditionary 
print(marks)
print(marks["puja"])

print(marks.get("soni"))
# print(marks["soni"])

# if key present in the dictionary then then marks.get("key") and marks["key"] will behave same but if key is not present in the dictionary then marks.get("key") will gave the result none  and 
# marks["keys"] will gave the error
