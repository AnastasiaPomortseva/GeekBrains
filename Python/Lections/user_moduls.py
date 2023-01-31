from class_user import User
from admin import Privileges,Admin

Admin=Admin('anna','erendel',18, 'Erendel')
print(Admin.describe_user())

Admin.privileges.show_privileges()