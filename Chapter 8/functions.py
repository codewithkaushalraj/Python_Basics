# function defination:
def cal_sum(a=0,b=0):  # 0 are the default val of both parameter if you want you can set default values
    # as you wish
    #  Default parameter ki value last se dena suru karte hai 
    print(f"The sum of {a} and {b} is : {a+b} ")
    return a+b

num1=int(input("Enter first number : "))
num2=int(input("Enter second number : "))

cal_sum(num1,num2) #function call :(arguments)