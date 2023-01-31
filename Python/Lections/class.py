# #class Dog():
#     """Easy dog's model"""
#
#     def  __init__(self, name, age):
#         """init atributs name and age"""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """Dog sit by command"""
#         print(f"{self.name} is now sitting")
#     def roll_over(self):
#         """dog roll over by command"""
#         print(f"{self.name} rolled over!")
#
# my_dog=Dog('Willie',6)
# print(f"My dog's name{my_dog.name}.")
# print(f"my_dog is {my_dog.age} years old.")
#


class User:
    """Информация о пользователе"""

    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city=city
        self.login_attempts=0
    def describe_user(self):
        "Выводит информацию с данными пользователя"
        describe = f"Пользователь: {self.first_name} , {self.last_name}, {self.age}, {self.city}"
        return describe.title()
    def col_login_attempts(self):
        """Display login attempts"""
        print(f"Login attempts: {self.login_attempts}")
    def update_login_attempts(self, attempts):
        self.login_attempts=attempts

    def increment_login_attempts(self, attempts_number):
        """Увеличивает значение количества попыток входа"""
        self.login_attempts += attempts_number
    def reset_login_attempts(self):
        """Обнуляет значение попыток входа"""
        self.login_attempts = 0

game_user=User('Ivan','Petrov','27','Moscow')
print(game_user.describe_user())

game_user.update_login_attempts(5)
game_user.col_login_attempts()

game_user.increment_login_attempts(3)
game_user.col_login_attempts()

game_user.reset_login_attempts()
game_user.col_login_attempts()