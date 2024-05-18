num_1 = int(input("Введите первое число: "))
znak = input("Что вы хотите сделать? ")
num_2 = int(input("Введите второе число: "))

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
else:
    print("Некорректная операция")

