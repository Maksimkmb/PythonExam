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


car1 = Car("Toyota", "Camry", 2022, 50)
car2 = Car("Honda", "Civic", 2021, 40)

client1 = Client("John", "Doe")
client2 = Client("Jane", "Smith")

rental1 = Rental(car1, client1, 3)
rental2 = Rental(car2, client2, 2)

print(rental1.reserve())
print(rental2.reserve())

print(f"Rental cost 1: {rental1.calculate_cost()} USD")
print(f"Rental cost 2: {rental2.calculate_cost()} USD")


def print_menu():
    print("1. Додати автомобіль")
    print("2. Додати клієнта")
    print("3. Зарезервувати автомобіль")
    print("4. Обчислити вартість оренди")
    print("5. Вийти")

# Приклад використання

cars = []
clients = []
rentals = []

while True:
    print_menu()
    choice = input("Введіть номер дії: ")

    if choice == "1":
        # Додавання автомобіля
        brand = input("Введіть марку автомобіля: ")
        model = input("Введіть модель автомобіля: ")
        year = int(input("Введіть рік випуску: "))
        rate = float(input("Введіть вартість оренди за день: "))
        car = Car(brand, model, year, rate)
        cars.append(car)
        print(f"Автомобіль {car} доданий")

    elif choice == "2":
        # Додавання клієнта
        first_name = input("Введіть ім'я клієнта: ")
        last_name = input("Введіть прізвище клієнта: ")
        client = Client(first_name, last_name)
        clients.append(client)
        print(f"Клієнт {client} доданий")

    elif choice == "3":
        # Резервування автомобіля
        print("Доступні автомобілі:")
        for i, car in enumerate(cars, start=1):
            print(f"{i}. {car}")

        car_choice = int(input("Виберіть номер автомобіля для резервування: ")) - 1

        for i, client in enumerate(clients, start=1):
            print(f"{i}. {client}")
        client_choice = int(input("Виберіть номер клієнта: ")) - 1

        rental = Rental(cars[car_choice], clients[client_choice], int(input("Введіть кількість днів оренди: ")))
        rentals.append(rental)
        print(rental.reserve())
        

    elif choice == "4":

        print("Доступні оренди:")
        for i, rental in enumerate(rentals, start=1):
            print(f"{i}. {rental}")

        rental_choice = int(input("Виберіть номер оренди для обчислення вартості: ")) - 1
        cost = rentals[rental_choice].calculate_cost()
        print(f"Вартість оренди: {cost} грн")

    elif choice == "5":
        print("па-па!")
        break

    else:
        print("введіть щось нормальне")