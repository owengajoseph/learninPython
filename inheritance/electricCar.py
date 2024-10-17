class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):

        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):

        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
             print("You can't roll back an odometer!")

    def increment_odometer(self, miles):

        self.odometer_reading += miles

# 1


class Battery():
    """A simple attempt to model a battery to an electric car."""
# 2

    def __init__(self, batterySize=70):
        """ininitialize the battery's attributes."""
        self.batterySize = batterySize

    def describeBattery(self):
        """print a statement describing the battey size."""
        print("this car has a " + str(self.batterySize)+"-KWH battery.")
    
    def getRange(self):
        """print a statement about the range this battery provides."""
        if self.batterySize==70:
            range=240
        elif self.batterySize==85:
            range=270
        
        message ="This car goes approximately "+ str(range)
        message+=" miles on a full charge"
        return message    


class ElectricCar(Car):
    """Represent aspects of car, specific to electric vehicles."""

# 3
    def __init__(self, make, model, year):
        """intialize attributes of the parent class. Then initialize attributes specific to an electric car"""

        super().__init__(make, model, year)
        # 4
        self.battery=Battery()
        #this line tells python to create a new instance of Battery of 70 , and store that instace in the attribute self.battery



# 5
myTesla = ElectricCar('tesla', 'model s', 2016)
print(myTesla.get_descriptive_name())
myTesla.battery.describeBattery()
print(myTesla.battery.getRange())