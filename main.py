"""import datetime as dt
now = dt.datetime.now()
then = dt.date(2011,12,11)
def print_(text):
    new_text = f"{text.month}-{text.day}-{text.year}"
    return new_text
now = now.strftime("%m/%d/%Y, %H:%M:%S")
print(now)
"""
import datetime as dt
class BikeRental:
    def __init__(self,stock):
        """ Initializer for the stock"""
        self.__stock = stock

    @property
    def display(self):
        """Displays the bikes that are currently available in the station """
        return self.__stock
    @display.setter
    def set_bike_number(self,n):
        if n < 0:
            self.__stock += n
        else:
            self.__stock += n
    def rent_bike_on_hourly_basis(self,n):
        """Rent a bike on hourly basis"""
        if n <= 0:
            print("Can only rent a positive number of bikes. ")
            return None
        elif n > self.display:
            print(f"There are {self.display} bikes available for rent, please only select a number up to the amount available.")

        else:
            now = dt.datetime.now()
            print(f"You have rented {n} number of bikes today at {now.hour}:{now.minute}:{now.second}")
            print("You will be charged $5 for each hour you spend on the bike")
            print("We hope that you enjoy our services!!")
            self.set_bike_number = -n
            return now
    def rent_bikes_on_daily_basis(self,n):
        """Rent bikes on daily bases. """
        if n <= 0:
            print("You can only rent positive numbers of bikes")
            return None
        elif n > self.display:
            print(f"There are {self.display} bikes available for rent, please only select a number that is less than or up to the amount available.")
            return None
        else:
            now = dt.date.today()
            print(f"You have rented a bike on daily basis at {now.month}/{now.day}/{now.year}")
            print("You will be charged $20 daily")
            print("We hope that you enjoy our services!!")
            self.set_bike_number = -n
            return now
    def rent_bikes_on_weekly_basis(self,n):
        """Rent bikes on weekly basis"""
        if n <= 0:
            print("You can only rent positive numbers of bikes.")
            return None
        elif n > self.display:
            print(f"There are {self.display} bikes available in the station. Please select a positive number that is less than or up to the amount available. ")
            return None
        else:
            now = dt.date.today()
            print(f"You have rented a bike on weekly basis at {now}")
            print("You will be charged $60 weekly")
            print("We hope that you enjoy our services!!")
            self.set_bike_number = -n
            return now
    def return_bike(self,requests):
        """Returns the bike into the system, increases the number of bikes in the system and gives the customer their bills. """
        rental_time, rental_basis, num_of_bikes = requests
        if rental_time and rental_basis and num_of_bikes:
            now = dt.datetime.now()
            rental_period = now - rental_time
            #Hourly rental calculation
            if rental_basis == 1:
                amount = rount((rental_period / 3600) * 5 * num_of_bikes)
            #Daily rental calculation
            elif rental_basis == 2:
                amount = round(rental_period.days * num_of_bikes * 20)
            elif rental_basis == 3:
                amount = round(rental_period.days / 7 * num_of_bikes * 60)
            if num_of_bikes >= 3 and num_of_bikes <= 6:
                print("You are eligible for family discount promotion ")
                amount *= 0.7
            self.set_bike_number == num_of_bikes
            print("Thanks for returning the bikes. Hope you enjoyed them! ")
            print(f"The bill is ${amount}")
            return amount
        else:
            print("Are you sure you rented a bike with us. ")
            return None


class Customer:
    def __init__(self):
        """Initialize variables in the customer class"""
        self.bikes = 0
        self.rental_basis = 0
        self.rental_time = 0
        self.bill = 0
    def request_bike(self):
        """Takes a request from the customer for the number of bikes"""
        bikes = input("Enter the number of bikes you would like to rent: ")
        try:
            bikes = int(bikes)
        except ValueError:
            print("The number of bikes has to be a positive integer!!")
            return -1
        bikes = int(bikes)
        if bikes <= 0:
            print("The number of bikes has to be a positive integer!!")
        else:
            self.bikes = bikes
        return self.bikes
    def return_bikes(self):
        """Allows customer to the rental shop"""
        if self.rentail_basis and self.rental_time and self.bill:
            return self.rental_time, self.rental_basis, self.bikes
        else:
            return 0,0,0


customer = Customer()
customer.request_bike()
print(customer.bikes)

