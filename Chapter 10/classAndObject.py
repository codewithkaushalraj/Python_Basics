# in python constructor is __init__ this will always be execute agar  nahi likha to python khud ka init function bna lega
# class Student:
#     name="Kaushal Raj" 

# Default Constructor
#     def __init__(self):
#         print("adding new student in a database.......")

# self aways be pointed to the object created 
# s1= Student()  # jaise hi s1 object bna constructor automatically call ho jayega self isi s1 ko point karega
# print(type(s1),s1.name)


class Student:
    #Parameterized Constructor
    def __init__(self,fullname):
        self.name=fullname
        print("adding new student in a database.......");
    
    def greet(self):
        print("Welcome ", self.name)
s1= Student("kaushal")
print(s1.name) 
s1.greet()
s2= Student("Keshav")
print(s2.name) 

class customer:
    def __init__(self, customer_name,Rating):
        print("Customer Details fetch Successfully ...")
        self.name=customer_name
        self.rate=Rating;

c1=customer("Sukhveer",2)
print(c1.name)
print(c1.rate)
c2=customer("Shalu",4.5)
print(c2.name)
print(c2.rate)
c3=customer("gyan",43.8)
print(c3.name)
print(c3.rate)
    