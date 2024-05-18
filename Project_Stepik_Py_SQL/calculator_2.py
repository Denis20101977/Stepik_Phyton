num_1 = input("Введите первое число: ")
num_2 = input("Введите второе число: ")
znak = input("Что вы хотите сделать? ")

# Проверка на корректность ввода чисел
if not num_1.isdigit() or not num_2.isdigit():
    print("Ошибка: Введите числа")
elif znak not in ['+', '-', '*', '/']:
    print("Ошибка: Введите один из символов '+', '-', '*', '/'")
else:
    num_1 = int(num_1)
    num_2 = int(num_2)

    if znak == "+":
        print(num_1 + num_2)
    elif znak == "*":
        print(num_1 * num_2)
    elif znak == "-":
        print(num_1 - num_2)
    elif znak == "/":
        try:
            print(num_1 / num_2)
        except ZeroDivisionError:
            print("Ошибка: деление на ноль")

