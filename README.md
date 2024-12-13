class Vehicle:
def **init**(self, wheel_size, wheel_number):
self.wheel_size = wheel_size
self.wheel_number = wheel_number

    def go(self):
        return "vrrrrrrrooom!"

    def fill_up_tank(self):
        return "filling up!"

class Car(Vehicle): # Car is a subclass of Vehicle
def go(self): # Overriding the inherited method
return "VRRROOOOOOOOOOOM!!!!!"
