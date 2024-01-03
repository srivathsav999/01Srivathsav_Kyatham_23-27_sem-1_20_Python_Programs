class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee:
    def __init__(self, employee_id, job_title):
        self.employee_id = employee_id
        self.job_title = job_title

    def display_employee_info(self):
        print(f"Employee ID: {self.employee_id}, Job Title: {self.job_title}")

class Student:
    def __init__(self, student_id, major):
        self.student_id = student_id
        self.major = major

    def display_student_info(self):
        print(f"Student ID: {self.student_id}, Major: {self.major}")

class PersonInfo(Employee, Student):
    def __init__(self, name, age, employee_id, job_title, student_id, major):
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, job_title)
        Student.__init__(self, student_id, major)

    def display_person_info(self):
        self.display_info()
        self.display_employee_info()
        self.display_student_info()

# Example usage:
person_info = PersonInfo(name="John Doe", age=30, employee_id="E123", job_title="Developer", student_id="S456", major="Computer Science")
person_info.display_person_info()
