from class_user import User
"""Информация об админе и привелегиях админа"""
class Privileges():
    """display admin's privileges"""
    def __init__(self):
        self.admin_privileges = ["разрешено добавлять сообщение", "разрешено банить пользователей",
                            "разрешено удалять пользователей"]

    def show_privileges(self):

        print(f"Возможности администратора: {self.admin_privileges}")


class Admin(User):
    """Display information for admin"""

    def __init__(self, first_name, last_name, age, city):
        """jkj"""
        super().__init__(first_name, last_name, age, city)
        self.login_attempts = 0
        self.privileges = Privileges()




