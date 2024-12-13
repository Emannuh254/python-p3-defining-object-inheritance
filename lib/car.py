from vehicle import Vehicle  # Import Vehicle class

class Car(Vehicle):  # Inherit from Vehicle
    def __init__(self, wheel_size, wheel_number):  # Accept parameters in __init__
        super().__init__(wheel_size, wheel_number)  # Call the parent class constructor

    def go(self):  # Override go() method
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"
