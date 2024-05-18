class Cat():
    def __init__(self, color, poroda, age):
        self.color = color
        self.poroda = poroda
        self.age = age
        print("Кот создан")

    def mew(self):
        print(self.poroda + " мяукает")
    def sleep(self):
        print(self.poroda + " спит")

murka = Cat("Black", "Sibirskiy", 2)
murzik = Cat("White", "Siamskiy", 5)

murka.mew()
murzik.sleep()

