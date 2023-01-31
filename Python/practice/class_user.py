"""Modul User"""
class User:
    """Информация о пользователе"""

    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        "Выводит информацию с данными пользователя"
        describe = f"Пользователь: {self.first_name} , {self.last_name}, {self.age}, {self.city}"
        return describe.title()

    def col_login_attempts(self):
        """Display login attempts"""
        print(f"Login attempts: {self.login_attempts}")

    def update_login_attempts(self, attempts):
        self.login_attempts = attempts

    def increment_login_attempts(self, attempts_number):
        """Увеличивает значение количества попыток входа"""
        self.login_attempts += attempts_number

    def reset_login_attempts(self):
        """Обнуляет значение попыток входа"""
        self.login_attempts = 0


