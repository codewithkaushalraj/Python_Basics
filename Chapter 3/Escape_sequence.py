str="Kaushal Raj is a good Boy\nHe want to became a \tNo.1 \"software Developer\"";
print(str)
# String are immutable which means that you can not change them by running function on them
# name=input("Enter Your Name : ");
# print("Welcome : ",name)
# # Modern way to print the name 
# print(f"welcome {name}")

str2='''
name
You will get a  internship on date
'''
print(str2.replace("name","kaushal raj").replace("date","10-12-2026"));

# double space detector : it will gave the idx where your character is present
print(str2.find("  "))
print(str2.replace("  "," "))