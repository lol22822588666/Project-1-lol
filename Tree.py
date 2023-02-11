class tree():
    def __init__(self, kind, age, hight):
        self.default_kind = oak
        self.default_age = 10
        self.default_hight = 2
    def grown(self, age, hight):
        print("Kind: ", self.kind)
        print("Age: ", self.age)
        print("Hight: ", self.hight)
        self.age += 1
        self.hight += 1
class fruit_tree(tree):
    def fruit(self, fruit):
        self.fruit = input("Is it fruit tree? y/n?:")
        if fruit == "y":
            print("This is the fruit tree")
        else:
            print("The tree has no fruit")
    try:
        input("Is it fruit tree? y/n?:")
    except:
        print("ОШИБКА 0000")