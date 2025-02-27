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
        return self.rental_price_per_day * days
    
    def get_rental_price(self):
        return self.__rental_price_per_day
    
    def set_rental_price(self, price):
        if price > 0:
            self.__rental_price_per_day = price
        else:
            print("Invalid price")

class Car(Vehicle):
    
    def __init__(self, brand, module, year, rental_price_per_day, seating_capacity, engine_capacity, transmission):
        super().__init__(brand, module, year, rental_price_per_day, seating_capacity, engine_capacity)
        self.transmission = transmission
    
    def display_info(self):
        super().display_info()
        print(f"Transmission: {self.transmission}")