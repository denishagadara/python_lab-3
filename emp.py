class Employee:
    def __init__(self, name, date_of_join, designation, salary):
        self.name = name
        self.date_of_join = date_of_join
        self.designation = designation
        self.salary = salary

    def display_employee_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Date of Joining: {self.date_of_join}")
        print(f"Designation: {self.designation}")
        print(f"Salary: ${self.salary:.2f}")

employee1 = Employee(
    name="John Doe",
    date_of_join="2023-01-15",
    designation="Software Engineer",
    salary=75000.00
)

employee1.display_employee_info()


