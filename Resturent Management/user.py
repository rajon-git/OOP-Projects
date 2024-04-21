# 1 Customer
# 2 Employee
# 3 Employee

#impoprt abstract base class
from abc import ABC

class User(ABC):  #in here user class inherit the ABC that's why now called it to base class
    def __init__(self,name,phone,email,address):
        super().__init__()
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address
        

class Employee(User):
    def __init__(self, name, phone, email, address,age,designation,salary):
        super().__init__(name, phone, email, address)
        self.age=age
        self.designation=designation
        self.salary=salary

# emp = Employee("rahim",123456,"rahim@gmail.com","Dhaka",34,'Manager',20000)
# print(emp.age)

class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.employees = []  #database

    def add_employee(self,name,phone,email,address,age,designation,salary):
        employee= Employee(name,phone,email,address,age,designation,salary) #employee classe  ekta object touri holo
        self.employees.append(employee)
        print(f"{name} is added")
    
    def view_employee(self):
        print("Employee Lists:-----")
        for emp in self.employees:
            print(f"Name: {emp.name}, Phone: {emp.phone}, Email: {emp.email}, Address: {emp.address}, Age: {emp.age}, Designation: {emp.designation}, Salary: {emp.salary}")

ad =Admin("Karim",123444,"karim@gmail.com","Dhaka")
ad.add_employee("Rajon",3333333,"rajon@gmail.com","dahaka",32,'Manager',20000)
ad.view_employee()