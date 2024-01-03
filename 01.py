# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
from datetime import datetime

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = datetime.strptime(dob, "%Y-%m-%d")

    def calculate_age(self):
        today = datetime.now()
        age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return age


person1 = Person("Gagan Nagu", "India", "2006-06-15")

print(f"Name: {person1.name}")
print(f"Country: {person1.country}")
print(f"Date of Birth: {person1.dob.strftime('%Y-%m-%d')}")

age = person1.calculate_age()
print(f"Age: {age} years")
