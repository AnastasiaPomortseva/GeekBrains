"""Класс для представления автомобиля"""
class Car:
    """Easy car's model"""

    def __init__(self, make, model, year):
        """init attributes describe of car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometr_reading = 0

    # def equals(self, car):
    #     if self.make == car.make and self.model == car.model and self.year == car.year and self.odometr_reading == car.odometr_reading:
    #         return print("Cars is equals")
    #     else:
    #         return print("Cars is not equals")

    def get_descriptive_name(self):
        """Returns a neatly formatted description"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def reed_odometr(self):
        """Display car mileage in miles"""
        print(f"This car has {self.odometr_reading} miles on it.")

    def update_odometr(self, mileage):
        """Устанавливает заданное значение на одометре
        При попытке обратной прокрутки изменение отклоняется"""
        if mileage >= self.odometr_reading:
            self.odometr_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Увеличивает показания одоментра с заданным приращением"""
        if miles >= 0:
            self.odometr_reading += miles
        else:
            print("You can't roll back on odometer!")





