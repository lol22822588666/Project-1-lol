class Phone:
    def __init__(self):
        self.isWorking = False
    def work(self):
        self.isWorking = True
    def call(self):
        if self.isWorking:
            print("Вам звонят")
    def info(self):
        print("Вкл", self.isWorking)
class PhoneMobile:
        def __init__(self):
            super().__init__()
            self.battery = 0
        def charge(self, procents):
            self.battery = procents
            print("Заряд: ", self.battery, "%")
        def info(self):
            print("Вкл", self.isWorking)
    def poli():
        for i in Phone, PhoneMobile:
            i().info()
print(poli())

#tel1 = Mobile()
#tel1.work()
#tel1.call()
#tel1.charge(59)