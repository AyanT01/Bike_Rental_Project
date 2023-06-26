import datetime
class BikeRental:
    def __init__(self,bikes):
        self.__bikes = bikes
    @property
    def bikes(self):
        """Gets the number of bikes available in the stations"""
        return self.__bikes
    def display_stock(self):
        print(f"There are {self.bikes} bikes available in the system.")
    @bikes.setter
    def bikes(self,n):
        """Updates the bikes in the station."""
        self.__bikes += n
    def rent_on_hourly_basis(self,num_of_bikes):
        """Rents bikes to customers on hourly basis and returns the time"""
        if num_of_bikes <= 0:
            print("You can only rent a positive number of bikes.")
        elif num_of_bikes > self.bikes:
            print(f"You can only rent up to the number of bikes available which is {self.bikes}")
            return None
        else:
            now = datetime.datetime.now()
            print(f"You have rented {num_of_bikes} on hourly basis at {now}")
            self.bikes = -num_of_bikes
            return now

    def rent_on_daily_basis(self,num_of_bikes):
        """Rents bikes to customers on daily basis and returns the time"""
        if num_of_bikes <= 0:
            print("You can only rent a positive number of bikes.")
        elif num_of_bikes > self.bikes:
            print(f"You can only rent up to the number of bikes available which is {self.bikes}")
            return None
        else:
            now = datetime.datetime.today()
            print(f"You have rented {num_of_bikes} on daily basis at {now}")
            self.bikes = -num_of_bikes
            return now

    def rent_on_weekly_basis(self,num_of_bikes):
        """Rents bikes to customers on weekly basis and returns the time"""
        if num_of_bikes <= 0:
            print("You can only rent a positive number of bikes.")
        elif num_of_bikes > self.bikes:
            print(f"You can only rent up to the number of bikes available which is {self.bikes}")
            return None
        else:
            now = datetime.datetime.today()
            print(f"You have rented {num_of_bikes} on hourly basis at {now}")
            self.bikes = -num_of_bikes
            return now

    def return_bikes(self,requests):
        rental_time, rental_basis, num_of_bikes = requests
        if rental_time and rental_basis and num_of_bikes:
            if rental_basis == 1:
                #Total Hourly bill
                bill = round((rental_time.second/3600) * 5 * num_of_bikes)
            elif rental_basis == 2:
                #Total daily bill
                bill = round((rental_time.day/24) * 20 * num_of_bikes)
            elif rental_basis == 3:
                #Total weekly bill
                bill = round((rental_time.day/7)* 60 * num_of_bikes)
            print("Thanks for renting with us, we hope you enjoyed our services!! ")
            print(f"Your bill is {bill}")
            return bill
        else:
            print("Are you sure you rented with us? ")
            return None

class Customer:
    def __init__(self):
        self.__bikes = 0
        self.__rental_basis = 0
        self.__rental_time = 0
        self.__bill = 0
    @property
    def bikes(self):
        return self.__bikes
    @bikes.setter
    def bikes(self,n):
        self.__bikes = n
    @property
    def rental_basis(self):
        return self.__rental_basis
    @rental_basis.setter
    def rental_basis(self,n):
        self.__rental_basis = n
    @property
    def rental_time(self):
        return self.__rental_time
    @rental_time.setter
    def rental_time(self,n):
        self.__rental_time = n
    @property
    def bill(self):
        return self.__bill
    @bill.setter
    def bill(self,n):
        self.__bill = n
    def request_bikes(self):
        bikes = input("How many bikes would you like to rent today: ")
        try:
            bikes = int(bikes)
        except ValueError:
            print("Number of bikes must be a positive integer")
            return -1
        if bikes <= 0:
            print("Can only request a positive number of bikes")
            return 0
        else:
            self.bikes = bikes
        return self.bikes
    def return_bikes(self):
        if self.rental_time and self.rental_basis and self.bikes:
            return self.rental_time, self.rental_basis, self.bikes
        else:
            return 0,0,0

Bike_system = BikeRental(100)
customer = Customer()
while True:
    print("""
    ====== Bike Rental App ======
    1. Display available bikes 
    2. Rent bikes on hourly basis --> $5 per hour 
    3. Rent bikes on daily basis --> $20 per day
    4. Rent bikes on weekly basis --> $60 per week
    5. Return bikes 
    6. Exit
    """)
    choice = input("Enter choice: ")
    try:
        choice = int(choice)
    except ValueError:
        print("Choice must be a number between 1-6. ")
        continue
    if choice == 1:
        Bike_system.display_stock()
    elif choice == 2:
        requested_bikes = customer.request_bikes()
        rental_time = Bike_system.rent_on_daily_basis(requested_bikes)
        customer.rental_time = rental_time
        customer.rental_basis = 1

    elif choice ==3 :
        requested_bikes = customer.request_bikes()
        rental_time = Bike_system.rent_on_daily_basis(requested_bikes)
        customer.rental_time = rental_time
        customer.rental_basis = 2
    elif choice == 4:
        requested_bikes = customer.request_bikes()
        rental_time = Bike_system.rent_on_weekly_basis(requested_bikes)
        customer.rental_time = rental_time
        customer.rental_basis = 3
    elif choice == 5:
        request_tuple = customer.return_bikes()
        print(request_tuple)
        bill = Bike_system.return_bikes(request_tuple)
        customer.bill = bill
        customer.rental_time, customer.rental_basis, customer.bill = 0,0,0
    elif choice == 6:
        break
    else:
        print("Invalid input, Please enter a number between 1 and 6")
print("Thanks for using the bike rental system!")




