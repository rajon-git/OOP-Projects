#Entities: Book, User, Library
#Functionalities: adding user, adding books, borrow,return

class Book:
    def __init__(self,cat,id,name,quantity):
        self.id=id
        self.name=name
        self.cat=cat
        self.quantity=quantity

class User:
    def __init__(self,id,name,password):
        self.id=id
        self.name=name
        self.password=password
        self.borrowedBooks=[]
        self.returnedBooks=[]

class Library:
    def __init__(self,owner,name):
        self.owner=owner
        self.name=name
        self.books=[]
        self.users=[]

    def addBook(self,cat,id,name,quantity):
        book = Book(cat,id,name,quantity)
        self.books.append(book)

        print(f"\n\t{name} book added successfully!!")
    
    def addUser(self,id,name,password):
        user = User(id,name,password)
        self.users.append(user)
        return user
    
    def borrowBook(self,user,id):
        for book in self.books:
            if book.id == id:
                if book in user.borrowedBooks:
                    print("\n\tAlready Borrowed!!")
                    return
                elif book.quantity < 1:
                    print("\n\tNo copies available!!")
                    return
                else:
                    user.borrowedBooks.append(book)
                    book.quantity -= 1
                    print(f"\n\t{book.name} borrowed successfully!!")
                    return
        print(f"\n\tBook not found!!")  

    def showUsers(self):
        print("\n\tList of Users-----")  
        for user in self.users:
            print(f"\tID: {user.id}, Name: {user.name}")

    def showBooks(self):
        print("\n\tList of Books-----")  
        for book in self.books:
            print(f"\tID: {book.id}, Name: {book.name}, Category: {book.cat}, Quantity: {book.quantity}") 
        


pl = Library("Rajon", "Phitron Library")
admin = pl.addUser(1,'admin', 'admin')
rajon = pl.addUser(22,'Rajon','1234')
pyBook = pl.addBook('Sici-Fi',22,'Dune',10)

run = True
currentUser=admin

while run:
    if currentUser == None:
        print(f"\n\tNo logged in User!!")
        option = input("Login ? Registration (L/R): ")
        if option == 'R':
            id=int(input("\tEnter id: "))
            name= input("\tEnter Name: ")
            password= input("\tEnter Password: ")

            user=pl.addUser(id,name,password)
            currentUser=user
        elif option == 'L':
            id=int(input("\tEnter id: "))
            password= input("\tEnter Password: ")

            match = False
            for user in pl.users:
                if user.id == id and user.password==password:
                    currentUser=user
                    match=True
                    break

            if match==False:
                print(f"\n\tNo User Found!!")

    else:
        if currentUser.name == 'admin':
            print("Options: \n")
            print("1: Add Book")
            print("2: Show Users")
            print("3: Show Books")
            print("4: logout")

            ch = int(input("\nEnter Option: "))

            if ch == 1:
                 cat=input("\tEnter category: ")
                 id=int(input("\tEnter id: "))
                 name= input("\tEnter Name: ")
                 quantity= int(input("\tEnter quantity: "))

                 pl.addBook(cat,id,name,quantity)
            
            elif ch==2:
                pl.showUsers()

            elif ch==3:
                pl.showBooks()
                
            elif ch==4:
                currentUser=None

        else:
            print("Options: \n")
            print("1: Borrow Book")
            print("2: Return Users")
            print("3: Show Books")
            print("4: Show Borrowed Books")
            print("5: Show Returned Books")
            print("6: logout")

            ch = int(input("\nEnter Option: "))

            if ch==1:
                id=int(input("\tEnter id: "))
                pl.borrowBook(currentUser,id)

