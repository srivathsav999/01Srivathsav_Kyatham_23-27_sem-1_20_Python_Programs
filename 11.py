class Vehicle:
    def drive(self):
        print("Generic vehicle is being driven.")

class Car(Vehicle):
    def drive(self):
        print("Car is being driven.")

class Bicycle(Vehicle):
    def drive(self):
        print("Bicycle is being pedaled.")

# Example usage:
generic_vehicle = Vehicle()
generic_vehicle.drive()  # Output: Generic vehicle is being driven.

car = Car()
car.drive()  # Output: Car is being driven.

bicycle = Bicycle()
bicycle.drive()  # Output: Bicycle is being pedaled.
