# todo При помощи функции format мы можем подставить значение переменной которое встанет в фигурные скобки.

# name = "Alex"
# name = "Ivan"
# a = "Hello {}"
# result = a.format(name)
# print(result)

# first_name = "Иван"
# last_name = "Иванов"
# third_name = "Иванович"
# age = 30
# a = '{} {} {}'
# result = a.format(first_name, last_name, third_name)
# print("Меня зовут: " + result)

# todo  При помощи функции "f" мы делаем тоже самое что и выше но код получается компактнее

# result = f'{first_name} {last_name} {third_name} {str(age)}'
# print("Меня зовут: " + result)

name_1 = "Alex"
name_2 = "Ivan"
age = 30
print("Меня зовут: " + f'{name_1} {name_2}' + " мне: " + f'{age}' + " лет!")

