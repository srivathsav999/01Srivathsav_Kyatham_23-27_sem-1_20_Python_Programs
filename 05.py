class Vehicle:
    # Class attribute with a default value
    color = "white"

    def __init__(self, make, model, year, seating_capacity):
        self.make = make
        self.model = model
        self.year = year
        self.seating_capacity = seating_capacity

    def calculate_fare(self):
        # Default fare calculation for any vehicle
        return self.seating_capacity * 100

    def display_details(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Color: {self.color}")

class Bus(Vehicle):
    def __init__(self, make, model, year, seating_capacity):
        super().__init__(make, model, year, seating_capacity)

    def calculate_fare(self):
        # Calculate default fare for Bus
        base_fare = super().calculate_fare()

        # Add maintenance charge (10% of the base fare)
        maintenance_charge = 0.1 * base_fare

        # Total fare for Bus
        total_fare = base_fare + maintenance_charge

        return total_fare

# Example usage:
bus = Bus(make="Volvo", model="XYZ", year=2023, seating_capacity=50)

# Display details of the bus
bus.display_details()  # Output: Make: Volvo, Model: XYZ, Year: 2023, Color: white

# Calculate and display the fare for the bus
fare = bus.calculate_fare()
print(f"The total fare for the bus is: ${fare}")
