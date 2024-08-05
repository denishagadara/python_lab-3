class Company:
    def __init__(self, name, city, mobile_no):
        self.name = name
        self.city = city
        self.mobile_no = mobile_no

    def display_info(self):
        print(f"Company Name: {self.name}")
        print(f"City: {self.city}")
        print(f"Mobile No: {self.mobile_no}")

class Employee(Company):
    def __init__(self, name, city, mobile_no, emp_name, designation, salary):
        super().__init__(name, city, mobile_no)
        self.emp_name = emp_name
        self.designation = designation
        self.salary = salary

    def display_info(self):
        super().display_info()
        print(f"Employee Name: {self.emp_name}")
        print(f"Designation: {self.designation}")
        print(f"Salary: ${self.salary:.2f}")

employee1 = Employee(
    name="Tech Solutions Inc.",
    city="New York",
    mobile_no="123-456-7890",
    emp_name="Alice Johnson",
    designation="Software Developer",
    salary=85000.00
)

employee1.display_info()
