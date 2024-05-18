# def identefication(name):
#     print("Вы являетесь")
#
#     if name == "Alex":
#         print("Автором")
#
#     else:
#         print("Студентом")
#
#
# name = input("Введите свое имя: ")
# identefication(name)

#
# def identefication(name):
#     print("Вы являетесь")
#
#     if name == "Alex":
#         result = "Автором"
#
#     else:
#         result = ("Студентом")
#
#     return result
#
#
# name = input("Введите свое имя: ")
# # print(identefication(name))
# n = "Alex"
# s = identefication(name)
# print(n + s)


def identefication(name):
    print("Вы являетесь")

    if name == "Alex":
        result = "Автором"

    else:
        result = ("Студентом")

    return result


def status(result):
    print(result)


name = input("Введите свое имя: ")

status(identefication(name))
