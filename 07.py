class Object:
    def __init__(self, color):
        self.color = color

class Converse(Object):
    def __init__(self, color, low_or_high_top, tongue_color):
        super().__init__(color)
        self.low_or_high_top = low_or_high_top
        self.tongue_color = tongue_color
        self.brand = "Converse"

class CombatBoot(Object):
    def __init__(self, color, military_branch, desert_or_jungle):
        super().__init__(color)
        self.military_branch = military_branch
        self.desert_or_jungle = desert_or_jungle
        self.brand = "Combat Boot"

class Sandal(Object):
    def __init__(self, color, open_or_closed_toe, waterproof):
        super().__init__(color)
        self.open_or_closed_toe = open_or_closed_toe
        self.waterproof = waterproof
        self.brand = "Sandal"

# Example usage:
converse_object = Converse(color="Red", low_or_high_top="High", tongue_color="White")
combat_boot_object = CombatBoot(color="Black", military_branch="Army", desert_or_jungle="Desert")
sandal_object = Sandal(color="Brown", open_or_closed_toe="Open", waterproof=True)

# Display details of the objects
print("Details of Converse Object:")
print(f"Color: {converse_object.color}, Brand: {converse_object.brand}, Low or High Top: {converse_object.low_or_high_top}, Tongue Color: {converse_object.tongue_color}")

print("\nDetails of Combat Boot Object:")
print(f"Color: {combat_boot_object.color}, Brand: {combat_boot_object.brand}, Military Branch: {combat_boot_object.military_branch}, Desert or Jungle: {combat_boot_object.desert_or_jungle}")

print("\nDetails of Sandal Object:")
print(f"Color: {sandal_object.color}, Brand: {sandal_object.brand}, Open or Closed Toe: {sandal_object.open_or_closed_toe}, Waterproof: {sandal_object.waterproof}")
