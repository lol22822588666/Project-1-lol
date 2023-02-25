# def first(i):
#      def second():
#          print("hello")
#          i()
#          print("hi")
#      return second
# def third():
#      print("howdy")
#  #f=first(third)
#  #f()
# @first
# def result():
#      print("decorator")
# result()
def sandwitch(i):
    def osnova():
        print("Bulka")
        i()
        print("Sandwitch is gotov")
    return osnova
def ing(i):
    def nachinka():
        print("Kolbosa")
        i()
        print("Bumaga")
    return nachinka
@sandwitch
@ing
def dop():
     print("Sol`")
# sw=sandwitch(ing(dop))
# sw()
dop()
def lang(i):
     def name(*args, **kwargs):
         print("languages for program")
         print(args)
         print(kwargs)
         i(*args, **kwargs)
     return name
@lang
# def like():
#     print("I like assembler")
# like()
def like(x, y, z, asd = "liders"):
     print(x, y, z, asd)
like("js", "py", "c++", "IT market")
class File:
    def __init__(self, name):
         self.age=38
         self.name=name
    @lang
    def ege(self, my=-22):
         print("Ja kodil s", self.age+my)
f1 = File(name="Adolf")
f1.ege()

class ABOBA:
    def say():
        gerferfef = 6
        def display():
            print(gerferfef, "zamk")
        return display
    say()