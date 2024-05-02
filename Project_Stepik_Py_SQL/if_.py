pin_code = 1234
print("Введите пин-код")
user_pin = int(input())
if pin_code == user_pin:
    print("Ваш пин-код верный!")
else:
    print("Ваш пин-код неверный, у Вас осталось 2 попытки!")
    user_pin = int(input())
    if pin_code == user_pin:
        print("Ваш пин-код верный!")
    else:
        print("Ваш пин-код неверный, у Вас осталось 1 попытка!")
    user_pin = int(input())
    if pin_code == user_pin:
        print("Ваш пин-код верный!")
    else:
        print("Ваш пин-код неверный, Вы исчерпали все попытки!")
