# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
class Vehicle():
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage


car1 = Vehicle(180,20)
print(f"The max speed is {car1.max_speed} and \nit's mileage is {car1.mileage}")
