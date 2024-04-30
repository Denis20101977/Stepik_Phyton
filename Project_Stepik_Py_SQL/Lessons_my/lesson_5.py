# todo функция def - помогает многократно использовать код
# todo разобраться с return!!!
# num_1 = 10
# num_2 = 20
# result = num_1 + num_2
# print(result)
#
# num_1 = 30
# num_2 = 40
# result = num_1 + num_2
# print(result)
#
# def summ(num_1, num_2):
#     result = num_1 + num_2
#     print(result)
# summ("Hello", " world")

name = "Денис"
age = "35"
def hi(name, age):
    result = name + " " + age
    return result


h = hi(name, age)
print(h)



