# write a program to find out  whether a student pass or fail it requires a 40% and atleast 33% in each subject assume 3 subject and each subject  marks will be entered by the user

marks1=int(input("Enter a first subject marks :"))
marks2=int(input("Enter a second subject marks :"))
marks3=int(input("Enter a third subject marks :"))

total_percentage=(100*(marks1+marks2+marks3)/300)
if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are Pass with percentage : ",total_percentage)
else:
    print(" Oo! You are fail !! ")
