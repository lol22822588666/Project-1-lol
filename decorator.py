# def first(i):
#     def second():
#         print("hello")
#         i()
#         print("hi")
#     return second
# def third():
#     print("howdy")
# #f=first(third)
# #f()
# @first
# def result():
#     print("decorator")
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