# todo глобальные и локальные переменные!!!!

var_1 = int(input())  # ЭТО ГЛОБАЛЬНАЯ ПЕРЕМЕННАЯ!!!!
var_2 = int(input())  # ЭТО ГЛОБАЛЬНАЯ ПЕРЕМЕННАЯ!!!!


def summ():
    # var_1 = 30 # ЭТО ЛОКАЛЬНАЯ ПЕРЕМЕННАЯ!!!!
    # var_2 = 40 # ЭТО ЛОКАЛЬНАЯ ПЕРЕМЕННАЯ!!!!
    result = var_1 + var_2
    print(result)

def sub():
    # var_1 = 30 # ЭТО ЛОКАЛЬНАЯ ПЕРЕМЕННАЯ!!!!
    # var_2 = 40 # ЭТО ЛОКАЛЬНАЯ ПЕРЕМЕННАЯ!!!!
    result = var_1 - var_2
    print(result)


def sub_2():
    var_1 = 30 # ЭТО ЛОКАЛЬНАЯ ПЕРЕМЕННАЯ!!!!
    var_2 = 40 # ЭТО ЛОКАЛЬНАЯ ПЕРЕМЕННАЯ!!!!
    result = var_1 * var_2
    print("разность = " + str(result))

def sub_3 ():
    result = var_1 % var_2
    print("Остаток = " + str(result))

summ()
sub()
sub_2()
sub_3()

