"""Набор классов для представления электромобилей"""

from class_car import Car

class Battery():
    """Easy model by battery"""

    def __init__(self, battery_size=75):
        """Initiate attributs by battery """
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"this car has a {self.battery_size} - kWh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")
    def upgrade_battery(self):
        if self.battery_size <=100:
            self.battery_size = 100
        elif self.battery_size >=100:
            self.battery_size = 100
class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобиля"""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса родителя.Затем инициализирует атрибуты, специфичные для электромобиля"""
        super().__init__(make, model, year)
        self.battery = Battery()


