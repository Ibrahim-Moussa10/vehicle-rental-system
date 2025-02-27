class Vehicle:
    def __init__(self,brand, module, year, rental_price_per_day,seating_capacity, engine_capacity):
        self.brand = brand
        self.module = module
        self.year = year
        self.__rental_price_per_day = rental_price_per_day
        self.seating_capacity = seating_capacity
        self.engine_capacity = engine_capacity
    
    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Module: {self.module}")
        print(f"Year: {self.year}")
        print(f"Rental price per day: {self.__rental_price_per_day}")
        print(f"Seating capacity: {self.seating_capacity}")
        print(f"Engine capacity: {self.engine_capacity}")

    def rental_cost(self, days):
        return self.get_rental_price() * days
    
    def get_rental_price(self):
        return self.__rental_price_per_day
    
    def set_rental_price(self, price):
        if price > 0:
            self.__rental_price_per_day = price
        else:
            print("Invalid price")

class Car(Vehicle):

    def __init__(self, brand, module, year, rental_price_per_day, seating_capacity, engine_capacity):
        super().__init__(brand, module, year, rental_price_per_day, seating_capacity, engine_capacity)
    
    def display_info(self):
        super().display_info()
 

class Bike(Vehicle):
    def __init__(self, brand, module, year, rental_price_per_day, seating_capacity, engine_capacity):
        super().__init__(brand, module, year, rental_price_per_day, seating_capacity, engine_capacity)
    
    def display_info(self):
        super().display_info()


car = Car("Toyota", "Corolla", 2020, 50, 5, 2)
bike = Bike("Yamaha", "YZF-R3", 2021, 30, 2, 1)

car_rental_cost = car.rental_cost(3)
bike_rental_cost = bike.rental_cost(3)

print("================================================")
print("Car Details:")
car.display_info()
print("================================================")
print("Bike Details:")
bike.display_info()
print("================================================")
print(f"Car rental cost for 5 days: ${car_rental_cost}")
print(f"Bike rental cost for 5 days: ${bike_rental_cost}")
print("================================================")

car.set_rental_price(60)
bike.set_rental_price(25)

print("================================================")
print("Updated Rental Price:")
updated_car_rental_cost = car.rental_cost(3)
updated_bike_rental_cost = bike.rental_cost(3)
print(f"Updated Car rental cost for 3 days: ${updated_car_rental_cost}")
print(f"Updated Bike rental cost for 3 days: ${updated_bike_rental_cost}")
print("================================================")