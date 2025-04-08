class Vehicle:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")

class Car(Vehicle):
    def move(self):
        print(f"{self.name} is driving on the road 🚗💨")

class Airplane(Vehicle):
    def move(self):
        print(f"{self.name} is flying in the sky ✈️☁️")

class Boat(Vehicle):
    def move(self):
        print(f"{self.name} is sailing on the water ⛵🌊")

class Bicycle(Vehicle):
    def move(self):
        print(f"{self.name} is being pedaled on the path 🚲")

class Helicopter(Vehicle):
    def move(self):
        print(f"{self.name} is hovering in the air 🚁")

# Create instances of different vehicles
vehicles = [
    Car("Toyota Camry"),
    Airplane("Boeing 747"),
    Boat("Sailfish"),
    Bicycle("Mountain Bike"),
    Helicopter("Apache")
]

# Demonstrate polymorphic behavior
for vehicle in vehicles:
    vehicle.move()