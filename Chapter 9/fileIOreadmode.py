# f=open("filePath","Mode")
f = open("filedata.txt", "r")

# Read the eniter data
# data=f.read()

# cursor will maintain that usne kaha tak ka data read kar liya hai on next time bo wahi ke aage se data read karna start kar dega agar ek baar data pura read ho gya then next time readline chalance be only blank spaces print hongi

# read the number of character that you mention-1 
data=f.read(5) # read the 4 character from starting
print(data)

line1=f.readline() # On each time this will read the data line by line
print(line1)
line2=f.readline() # On this time second line data will be read
print(line2)
print(type(data))
f.close()

'''
r+ : read and overwrite pointer at start (No truncate)
w+ : write and  overwrite (complete data truncate)
a+ : read and append pointer will be at the end (No truncate )
'''
