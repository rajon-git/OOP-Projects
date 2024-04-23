# 1 Customer
# 2 Employee
# 3 Employee

#impoprt abstract base class
from abc import ABC
from orders import Order

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
        self.cart= Order()
        
    def view_menu(self,restaurant):
        restaurant.menu.show_menu()
        
    def add_to_cart(self,restaurant,item_name,quantity):
        item = restaurant.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("Item quantity exceeded!!")
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print("Item added")
        else:
            print("Item not found")
            
    def view_cart(self):
        print("********View cart*******")
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total Price: {self.cart.total_price}")
        
    def pay_bil(self):
        print(f"Total {self.cart.total_price} paid successfully")
        self.cart.clear()
        
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
        
    def view_items(self,restaurent):
        restaurent.menu.show_menu()
        