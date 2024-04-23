from food_item import FoodItem
from menu import Menu
from user import Customer,Admin,Employee
from restaurant import Restaurant
from orders import Order


mamar_restaurant = Restaurant("Mamar Restaurant")
def cutomer_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone")
    address = input("Enter your address")
    customer = Customer(name=name,email=email,phone=phone,address=address)
    
    while True:
        print(f"Wellcome {customer.name}!!")
        print("1. View Menu")
        print("2. Add Item To Cart")
        print("3. View Cart")
        print("4. Pay Bill")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        if choice == 1:
            customer.view_menu(mamar_restaurant)
        elif choice == 2:
            item_name = input("Enter item name: ")
            item_quantity = int(input("Enter item quantity: "))
            customer.add_to_cart(mamar_restaurant,item_name,item_quantity)
            
        elif choice == 3:
            customer.view_cart()
            
        elif choice == 4:
            customer.pay_bil()
        elif choice == 5:
            break
        else:
            print("Invalid Options")