class Car:
    def __init__(self, brand, model, year, price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.price_per_day = price_per_day
        self.reserved = False

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"

class Client:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Rental:
    def __init__(self, car, client, days_rented):
        self.car = car
        self.client = client
        self.days_rented = days_rented

    def reserve(self):
        if not self.car.reserved:
            self.car.reserved = True
            return f"{self.client} reserved {self.car}"
        else:
            return f"{self.car} is already reserved"

    def calculate_cost(self):
        return self.days_rented * self.car.price_per_day


car1 = Car("BMW", "C5", 2018, 5000)
car2 = Car("Audi", "Q6", 2019, 4000)

client1 = Client("John", "Doe")
client2 = Client("maksim", "Dukal")

rental1 = Rental(car1, client1, 3)
rental2 = Rental(car1, client2, 2)

print(rental1.reserve())
print(rental2.reserve())

print(f"Rental cost 1: {rental1.calculate_cost()} USD")
print(f"Rental cost 2: {rental2.calculate_cost()} USD")


