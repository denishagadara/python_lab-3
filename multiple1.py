# Base class 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"

# Base class 2
class Employee:
    def __init__(self, employee_id, position):
        self.employee_id = employee_id
        self.position = position

    def get_job_details(self):
        return f"Employee ID: {self.employee_id}, Position: {self.position}"

# Derived class that inherits from both Person and Employee
class Manager(Person, Employee):
    def __init__(self, name, age, employee_id, position, department):
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, position)
        self.department = department

    def get_manager_info(self):
        return f"{self.get_info()}, {self.get_job_details()}, Department: {self.department}"

# Creating an instance of Manager
manager = Manager("Alice Johnson", 35, "M12345", "Project Manager", "IT")

# Printing the manager's information
print(manager.get_manager_info())
