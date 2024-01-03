class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass  # Placeholder for the sound method

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self):
        return "Woof!"

    def wag_tail(self):
        print("Dog is wagging its tail.")

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        return "Meow!"

    def purr(self):
        print("Cat is purring.")

# Example usage:
dog = Dog(name="Buddy", age=3, breed="Labrador")
cat = Cat(name="Whiskers", age=2, color="Gray")

print(f"{dog.name} is {dog.age} years old. Breed: {dog.breed}")
print(f"{cat.name} is {cat.age} years old. Color: {cat.color}")

dog.make_sound()  # Output: Woof!
cat.make_sound()  # Output: Meow!

dog.wag_tail()    # Output: Dog is wagging its tail.
cat.purr()        # Output: Cat is purring.
