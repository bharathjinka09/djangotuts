class Car:
    def __init__(self, name, color, mileage):
        self.name = name
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"{self.name} car of {self.color} color with {self.mileage} mileage"


car1 = Car("Swift", "red", 320)
print(car1)
