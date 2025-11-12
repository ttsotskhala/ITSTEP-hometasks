class Car:
    number_of_cars = 0

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

        Car.number_of_cars += 1                    # ყოველი ობიექტის შექმნისას ვზრდით მთლიანი რაოდენობას

    def age_of_car(self):
        current_year = 2025
        return current_year - self.year

    def car_info(self):
        print(f"ბრენდი: {self.brand}")
        print(f"მოდელი: {self.model}")
        print(f"გამოშვების წელი: {self.year}")
        print(f"ავტომობილის ასაკი: {self.age_of_car()} წელი\n")

    @classmethod
    def total_cars(cls):
        print(f"მთლიანი შექმნილი მანქანების რაოდენობა: {cls.number_of_cars}")


# --- მემკვიდრე კლასი ---
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_life):
        super().__init__(brand, model, year)
        self.battery_life = battery_life

    def battery_info(self):
        print(f"ამ მანქანის ბატარეის ხანგრძლივობა არის {self.battery_life} საათი\n")


# --- ტესტირება ---
car1 = Car("Toyota", "RAV4", 2016)
car2 = Car("Opel", "Zafira", 2005)

e_car = ElectricCar("Tesla", "Model S", 2023, 16)

car1.car_info()
car2.car_info()
e_car.car_info()
e_car.battery_info()

Car.total_cars()
