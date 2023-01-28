import random

class Student:
    #print("Class Student")
    col=0
    def __init__(self, height=160, name=None, age=10):
        self.height=height
        self.name=name
        self.age=age
        Student.col+=1

    def grow(self,height=5):
        self.height+=height

    def __str__(self):
        return f"My name is {self.name}. \nI am {self.age}"

student1=Student(height=170, name="Anatoliy", age=14)
student1.grow(height=5)
print(student1.__str__())

student2=Student(height=160, name="Boris", age=15)
student2.grow(height=5)
print(student2.__str__())

print("First hight is",student1.height)
print("Second`s hight is",student2.height)
print(Student.col)
