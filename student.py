
#class Student:
#    #print("Class Student")
#    col=0
#    def __init__(self, height=160, name=None, age=10):
#        self.height=height
#        self.name=name
#        self.age=age
#        Student.col+=1

#    def grow(self,height=5):
#        self.height+=height

#    def __str__(self):
#        return f"My name is {self.name}. \nI am {self.age}"

#student1=Student(height=170, name="Anatoliy", age=14)
#student1.grow(height=5)
#print(student1.__str__())

#student2=Student(height=160, name="Boris", age=15)
#student2.grow(height=5)
#print(student2.__str__())

#print("First hight is",student1.height)
#print("Second`s hight is",student2.height)
#print(Student.col)
import random
from random import randint

class Student:
    def __init__(self,name):
        self.name=name
        self.happiness=50
        self.progress=0
        self.alive=True

    def study(self):
        print("It`s time to waste time in school")
        self.happiness-=10
        self.progress+=5
    def sleep(self):
        print("Time to waste time in bed")
        self.happiness-=1
    def rest(self):
        print("GAMING TIME")
        self.happiness+=10
        self.progress-=5
    def isAlive(self):
        if self.happiness<=0:
            print("Dead inside zxc ghoul")
            self.alive=False
        if self.progress>=20:
            print("You finished your academy")
            self.alive = True
            self.happiness+=15
        if self.progress<-10:
            print("You faild, now yor`re stupid")
            self.alive = False
    def day(self):
        print("Happines: ",self.happiness)
        print("Studyness: ", self.progress)
    def choice(self, numDay):
        numDay="Day #"+str(numDay)+"of your life"+self.name
        print(f"{numDay:=^50}")
        rnd=randint(1,3)
        if rnd==1: self.study()
        elif rnd==2: self.sleep()
        else: self.rest()
        self.day()
        self.isAlive()
student1=Student(name="Anatoliy")
for i in range(1,8):
    student1.choice(i)