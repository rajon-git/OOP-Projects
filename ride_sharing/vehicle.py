from abc import ABC

class Vehicle(ABC):
    speed = {
        'bike' : '60',
        'car' : '50',
        'cng' : '15'
    }
    def __init__(self,vehicle_type,rate,license_plate):
        self.vehicle_type=vehicle_type
        self.license_plate=license_plate
        self.rate=rate
        
class Car(Vehicle):
    def __init__(self, vehicle_type, rate, license_plate):
        super().__init__(vehicle_type, rate, license_plate)
        
class Bike(Vehicle):
    def __init__(self, vehicle_type, rate, license_plate):
        super().__init__(vehicle_type, rate, license_plate)