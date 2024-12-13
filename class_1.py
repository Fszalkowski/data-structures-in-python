class car():
    def brand(self, brand):
        print(f'Car brand: {brand}')
    def price(self, price):
        print(f'Car price: {price} euro')
    def milage(self, milage):
        print(f'Car milage: {milage} km')
new_car = car()

while True:
    try:
        querry_1 = str(input("Enter car brand: "))
        querry_2 = int(input("Enter car price(EUR): "))
        querry_3 = int(input("Enter car milage(KM): "))

    except ValueError:
        print("Invalid value")
        continue

    new_car.brand(querry_1)
    new_car.price(querry_2)
    new_car.milage(querry_3)
    break