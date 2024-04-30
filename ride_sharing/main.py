from ride import Ride,RideRequest,RideMatching, RideSharing
from users import Rider,Driver
from vehicle import Car,Bike

niye_jao = RideSharing("Niye Jao")
rahim = Rider("Rahim Uddin", "rahim@gmail.com", 1234567, "Mohakhali", 1200)
niye_jao.add_rider(rahim)

kolimuddin = Driver("Kolim Uddin", "kalim@gmail.com",2345678,"Gulshan")
niye_jao.add_driver(kolimuddin)

rahim.request_ride(niye_jao, "Uttara", "car")
rahim.show_current_ride()
kolimuddin.reach_destionation(rahim.current_ride)

print(niye_jao)