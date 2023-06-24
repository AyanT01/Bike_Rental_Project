"""import datetime as dt
now = dt.datetime.now()
then = dt.date(2011,12,11)
def print_(text):
    new_text = f"{text.month}-{text.day}-{text.year}"
    return new_text
now = now.strftime("%m/%d/%Y, %H:%M:%S")
print(now)
"""
class BikeRental:
    def __init__(self,stock):
        """ Initializer for the stock"""
        self.__stock = stock

    @property
    def display(self):
        """Displays the bikes that are currently available in the station """
        print(f"There are {self.__stock} bikes left in the station. ")
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
        elif n > self.__stock:
            print(f"There are {self.display} bikes available for rent, please only select a number up to the amount available.")
        else:
            self.set_bike_number = -n
            return self.__stock



bike = BikeRental(49)
print(bike.rent_bike_on_hourly_basis(5))


