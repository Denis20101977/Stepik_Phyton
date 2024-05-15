# list = [1, 4, 6, 9, 10, 12]
# for i in list:
#     if i == 6:
#         print("Ура 6")
#         break
#         print(i)

# login = input("Введите ваш логин! ")
# while True:
#     if login == "Alex":
#         print("Вы ввели верный логин")
#         password = input("Введите ваш пароль ")
#
#     else:
#         print("Вы ввели неверный логин")
#         break

list = [1, 4, 6, 9, 10, 12]
for i in list:
    if i == 12:
        print("Плохо 10")
        break
    elif i == 4:
        print("Ура 4")

    elif i == 6:
        print("Ура 6")
        continue

    print(i)








