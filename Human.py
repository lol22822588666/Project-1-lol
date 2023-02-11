class Human():
    def __init__(self, name, age):
        self.default_name = Anton
        self.default_age = 22
    def info(self, name, age, house, money):
        self.house = house
        self.money = money
    def default_info(self, house, money):
        self.default_house = house
        self.default_money = 100
    def make_deal(self):
