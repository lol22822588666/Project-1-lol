class Phone:
    def __init__(self):
        self.isWorking = False
    def work(self):
        self.isWorking = True
    def call(self):
        if self.isWorking:
            print("Вам звонят")
class Mobile(Phone):
        def __init__(self):
            super().__init__()
            self.battery = 0
        def charge(self, procents):
            self.battery = procents
            print("Заряд: ", self.battery, "%")
tel1 = Mobile()
tel1.work()
tel1.call()
tel1.charge(59)