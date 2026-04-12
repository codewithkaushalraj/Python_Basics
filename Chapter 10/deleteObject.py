
class Student:
    #Parameterized Constructor
    def __init__(self,fullname):
        self.name=fullname
        print("adding new student in a database.......");

s1=Student("Kaushal")
print(s1.name)
del s1.name
print(s1.name)
del s1
print(s1)
