num_1 = input("Введите первое число: ")
znak_1 = input("Что вы хотите сделать? ")
num_2 = input("Введите второе число: ")

# Проверка на корректность ввода чисел
if not num_1.isdigit() or not num_2.isdigit():
    print("Ошибка: Введите число")
elif znak_1 not in ['+', '-', '*', '/']:
    print("Ошибка: Введите один из символов '+', '-', '*', '/'")
else:
    num_1 = int(num_1)
    num_2 = int(num_2)

if znak_1 == "+":
    print(num_1 + num_2)
elif znak_1 == "*":
    print(num_1 * num_2)
elif znak_1 == "-":
    print(num_1 - num_2)
elif znak_1 == "/":
    try:
        print(num_1 / num_2)
    except ZeroDivisionError:
        print("На ноль не делим!")
# else:
#     print(" ")

