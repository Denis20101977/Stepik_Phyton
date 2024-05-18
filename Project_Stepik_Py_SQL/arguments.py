# def description(name, age, sex):
#     print(f"Имя: {name}, Возраст: {age}, Пол: {sex}")

# description("Анна", 30, "Woman") #Todo позиционный аргумент!!!

# description(name = "Анна", age = 30, sex =  "Woman") #Todo именованный аргумент!!!

n = "Анна"
a = 30
def description(name, age, sex):
    print(f"Имя: {name}, Возраст: {age}, Пол: {sex}")

description(n, a, "woman")