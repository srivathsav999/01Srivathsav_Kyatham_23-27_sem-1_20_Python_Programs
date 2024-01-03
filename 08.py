class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_details(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

# Create an object of the Car class
car_object = Car(make="Toyota", model="Camry", year=2022)

# Print the details of the car
car_object.display_details()
