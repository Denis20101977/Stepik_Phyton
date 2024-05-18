class Person():
    """Модель человека"""
    def __init__(self, name, age):
        """Инициализация атрибутов человека - имя и возраст"""
        self.name = name
        self.age = age
        print("Человек создан")

    def sing(self):
        """Просим человека спеть - это метод!"""
        print(self.name + " поет")

    def dance(self):
        """Просим человека станцевать"""
        print(self.name + " танцует")

man = Person("Алекс", 30)
woman = Person("Nastya", 30)
# print(man.name)

man.sing()
woman.dance()

