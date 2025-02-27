class Vehicle:
    def __init__(self,brand, module, year, rental_price_per_day):
        self.brand = brand
        self.module = module
        self.year = year
        self.rental_price_per_day = rental_price_per_day
    
    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Module: {self.module}")
        print(f"Year: {self.year}")
        print(f"Rental price per day: {self.rental_price_per_day}")