from Test import Opros
from random import randint

quest = ["Когда?", "Зачем?", "Кому?", "С какой целью?", "Куда?"]
print("Жмайте х чтобы ливнуть с позором")
while True:
    if not quest:
        print("Всё, довольно")
        break
    rnd = randint(0, len(quest)-1)
    myQ = Opros(quest[rnd])
    myQ.__str__()
    try:
        answer = input("Ответ: ")
    except:
        print("ОШИБКА 0000")
    if answer == "x":
        print("Всё, довольно")
        break
    myQ.save(answer)
    del quest[rnd]
print("Спасибо")
myQ.rez()