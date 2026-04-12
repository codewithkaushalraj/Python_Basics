age=int(input("Enter Your age : "))

# if elif else ladder
if(age>=18):
    print("You are eligible for vote")   # The starting space of line is called indentation
    print("Welcome")
elif(age<0):
    print("You are Entering a Invalid age")
else:
    print("You are not eligible for vote")
