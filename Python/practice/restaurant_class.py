"""Информация о ресторане"""
class Restaurant():
    """Information about restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Desplay information about type of restaurant"""
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe by restourant"""
        print(f"\nThis restaurant is named {self.name}")
        print(f"In this restourant {self.type} menu.")

    def set_number_served(self):
        """Desplay info about reservation"""
        print(f"Количество обслуженных посетителей: {self.number_served}")

    def upper_number_served(self, orders):
        """Устанавливает заданное значение количества посетителей"""
        if orders >= self.number_served:
            self.number_served = orders
        else:
            print("you cann't enter smaller number")

    def increment_number_served(self, clients):
     """Увеличивает показатель количества обслужанных посетителей"""
     self.number_served +=clients

    def open_restaurant(self):
     """information about the operating mode"""
     print(f"Restaurant {self.name} is opened.")
"""Информация о ресторане"""
class IceCreamStand(Restaurant):
    """Предоставляет информацию об асортименте мороженого в ресторане"""

    def __init__(self, restaurant_name, cuisine_type):
        """Инициализирует атрибуты класса родителя, затем новые атрибуты"""
        super().__init__(restaurant_name, cuisine_type)

    def flavour_list(self):
        """Display variants of flavours"""
        flavours=['apple','chocolate','strawberry','orange']
        print(f"В нашем ресторане представлены следующие вкусы мороженного: {flavours}")




