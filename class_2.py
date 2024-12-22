class car():
    def __init__(self,brand, model, production_year):
        self.brand = brand
        self.model = model 
        self.production_year = production_year
    def show_info(self):
        print(f"Car brand: {self.brand} Car model: {self.model} Car year: {self.production_year}")

new_car = car("Toyota", "Corolla", 2020)
new_car.show_info()