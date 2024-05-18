class Auto():

    def __init__(self, marka, color, speed):
        self.marka = marka
        self.color = color
        self.speed = speed

    def drive(self):
        print("Машина марки " + self.marka + " цвета " + self.color +  " едет со скоростью " + self.speed)

    def sky(self):
        print("Машина марки " + self.marka + " цвета " + self.color + " летит со скоростью " + self.speed)

bmw = Auto("Bmw", "Red", " 200" + " km/h")
audi = Auto("Audi", "Black", "300" + " km/h")

bmw.drive()
audi.sky()