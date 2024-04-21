class Hall:
    def __init__(self,rows,cols,hall_no):
        self._seats={}
        self.__hall_list=[]
        self._rows=rows
        self._cols=cols
        self._hall_no=hall_no

    def entry_hall(self,id,movie_name,time):
        hall=(id,movie_name,time)
        self.__hall_list.append(hall)
        seats= []
        for _ in range(self._rows):
            row=[]
            for _ in range(self._cols):
                seat = False  
                row.append(seat)
            seats.append(row)
        self._seats[id]=seats

    def book_seats(self, id, book_seat):
        if id not in self._seats:
            print("Invalid  ID")
            return
        seats =self._seats[id]
        cnt=0
        for seat in book_seat:
            row, col = seat
            if row < 0 or row >= self._rows or col < 0 or col >= self._cols:
                print(f"Invalid seat ({row}, {col})")
                continue
            if seats[row][col]:
                print(f"Seat ({row}, {col}) is already booked")
            else:
                seats[row][col] = True
                cnt += 1
                print(f"Seat ({row}, {col}) booked successfully")

    def view_hall_lists(self):
        print("\n\tShows Lists:")
        for movie in self.__hall_list:
            print(f"\ID: {movie[0]}, Movie Name: {movie[1]}, Time: {movie[2]}")

    def view_available_seats(self, id):
        if id not in self._seats:
            print("Invalid ID")
            return
        seats = self._seats[id]
        print("\n\tAvailable seats:")
        for i in range(self._rows):
            for j in range(self._cols):
                if not seats[i][j]:
                    print("O ", end="")  
                else:
                    print("X ", end="")  
            print() 

class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)


hall1 = Hall(rows=10, cols=10, hall_no=1)
hall1.entry_hall(id="111", movie_name="Matrix", time="10:00 AM")
hall1.entry_hall(id="222", movie_name="Inception", time="1:00 PM")
Star_Cinema.entry_hall(hall1)

run = True

while run:
    print("\nOptions:")
    print("1: View all shows today")
    print("2: View available seats")
    print("3: Book tickets")
    print("4: Exit")
    option = input("\nEnter your option: ")

    if option == "1":
        for hall in Star_Cinema.hall_list:
            hall.view_hall_lists()

    elif option == "2":
        id = input("Enter the show ID: ")
        for hall in Star_Cinema.hall_list:
            hall.view_available_seats(id)

    elif option == "3":
        id = input("Enter the show ID: ")
        seats = []
        while True:
            try:
                row=int(input("\tEnter row: "))
                col=int(input("\tEnter col: "))
                seats.append((row, col))
                break
            except ValueError:
                print("Invalid input. Please enter again.")
                continue
        for hall in Star_Cinema.hall_list:
            hall.book_seats(id, seats)
    elif option == "4":
        run = False
    else:
        print("Invalid option.")
