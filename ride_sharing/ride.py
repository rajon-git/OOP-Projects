from datetime import datetime
from vehicle import Car, Bike

class RideSharing:
    def __init__(self,company_name):
        self.company_name=company_name
        self.riders = []
        self.drivers = []
        self.rides = []
    def add_rider(self,rider):
        self.riders.append(rider)
    
    def add_driver(self,driver):
        self.drivers.append(driver)
    def __str__(self) -> str:
        return f"Company Name: {self.company_name} with riders {len(self.riders)} and drivers {len(self.drivers)}"

class Ride:
    def __init__(self,start_location,end_location,vehicle):
        self.start_location=start_location
        self.end_location=end_location
        self.driver=None
        self.rider=None
        self.start_time=None
        self.end_time=None
        self.estimated_fare=None
        self.vehicle=vehicle
        
    def set_driver(self,driver):
        self.driver=driver
        
    def start_ride(self):
        self.start_time=datetime.now()
        
    def end_ride(self):
        self.end_time=datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare
        
    def __repr__(self):
        return f"Ride Details. Started {self.start_location} to {self.end_location}"
    
class RideRequest:
    def __init__(self,rider,end_location):
        self.rider=rider
        self.end_location=end_location
        
class RideMatching:
    def __init__(self, drivers):
      self.available_drivers = drivers
      
    def find_driver(self,ride_request,vehicle_type):
        if len(self.available_drivers) > 0:
            print("Looking for divers....")
            driver = self.available_drivers[0]
            ride = Ride(ride_request.rider.current_location, ride_request.end_location)
            if vehicle_type == 'car':
                car = Car('Car','abu878',30)
            elif vehicle_type == 'bike':
                bike = Bike('Motor Bike', 'dggd677', 50)
            
            driver.accept_ride(ride)
            return ride
      