from random import randint

class Student:
    def __init__(self,name):
        self.name=name
        self.happiness=50
        self.progress=15
        self.money = 150
        self.alive=True

    def study(self):
        print("It`s time to waste time training")
        self.happiness-=10
        self.progress+=5
    def sleep(self):
        print("SLEEPING TIME")
        self.happiness+=1
    def rest(self):
        print("PLAYING TIME")
        self.happiness+=10
        self.progress-=5
    def isAlive(self):
        if self.happiness<=0:
            print("Dead inside zxc ghoul")
            self.alive=False
        if self.progress<-10:
            print("You faild, now yor`re stupid")
            self.alive = False
        if self.progress>=20:
            print("You won an award")
            self.alive = True
            self.happiness+=15
    def day(self):
        print("Happines: ",self.happiness)
        print("Studyness: ", self.progress)
    def choice(self, numDay):
        numDay="Day #"+str(numDay)+"of life of "+self.name
        print(f"{numDay:=^50}")
        rnd=randint(1,4)
        if rnd==1: self.study()
        elif rnd==2: self.sleep()
        else: self.rest()
        self.day()
        self.isAlive()
student1=Student(name="Sobak")
for i in range(1,8):
    student1.choice(i)