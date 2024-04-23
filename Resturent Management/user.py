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
        
class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart=None
        
    def view_menu(self,restaurant):
        restaurant.menu.show_menu()
        
    def add_to_cart(self,restaurant,item_name):
        item = restaurant.menu.find_item(item_name)
        if item:
            pass
        else:
            print("Item not found")
            
    def view_cart(self):
        print("********View cart*******")
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print("Total Price: {self.cart.total_price}")
class Order:
    def __init__(self):
        self.items={}
        
    def add_item(self,item):
        if item in self.items: 
            self.items[item] += item.quantity #cart e jodi already thake
        else:
            self.items[item] = item.quantity #cart e jodi na thake
    def remove(self,item):
        if item in self.items:
            del self.items[item]
            
    def total_price(self):
        return sum(item.price * quantity for item,quantity in self.items.items())
    
    def clear(self):
        self.items = {}
        
    
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

    def add_employee(self,restaurant,employee):
        restaurant.add_employee(employee)
    
    def view_employee(self,restaurant):
        restaurant.view_employee()
        
    def add_new_item(self,restaurent,item):
        restaurent.menu.add_menu_item(item)
        
    def remove_item(self,restaurent,item):
        restaurent.menu.remove_item(item)

class Restaurant:
    def __init__(self,name):
        self.name=name
        self.employees = []  #database
        self.menu = FoodItem()

    def add_employee(self,employee):
        self.employees.append(employee)

    def view_employee(self):
        print("Employee Lists:-----")
        for emp in self.employees:
            print(f"Name: {emp.name}, Phone: {emp.phone}, Email: {emp.email}, Address: {emp.address}, Age: {emp.age}, Designation: {emp.designation}, Salary: {emp.salary}")

class Menu:
    def __init__(self):
        self.items=[]
        
    def add_menu_item(self,item):
        self.items.append(item)

    def find_item(self,item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
            return None
        
    def remove_item(self,item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("Item Deleted Successfully")
        else:
            print("Item not found")
    
    def show_menu(self):
        print("*******Menu*********")
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")
            
class FoodItem:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity


mn=Menu()
item = FoodItem("Pizza",12.5,10)
mn.add_menu_item(item)
mn.show_menu()