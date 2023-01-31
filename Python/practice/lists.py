#famyly_names=['nastya','roma','taya']
#message=f'{famyly_names[0].title()} and {famyly_names[1].title()} are meread'
#print(message)

#cars=['kia', 'audi', 'geep','bmw']
#message=f'I want buy car by car brand {cars[3].upper()}'
#print(message)

#guests=['Мурзик','Мама','Лена']
#guests[2]='Шмелек'
#guests.insert(0, 'Жанна')
#guests.insert(1, 'Ваня')
#guests.append('Жанна')
#print(guests)
#print(f'Дорогой {guests[0]}, приглашаю тебя в гости!')
#print(f'Дорогая {guests[1]}, приглашаю тебя в гости!')
#print(f'Дорогой {guests[2]}, приглашаю тебя в гости!')
#print(f'Дорогой {guests[3]}, приглашаю тебя в гости!')
#print(f'Дорогой {guests[4]}, приглашаю тебя в гости!')

#pizzas=['сырная', 'жульен', 'пиперони']
#for pizza in pizzas:
#    print(f"В этом ресторане очень вкусная пицца {pizza}")

#print('\nЗакажите их все!')

#cube=[value**3 for value in range(1,11)]
#print(cube)

#def display_message(lesson):
#    """Передача сообщения по теме лекции"""
#    print(f" задачи в этой главе по теме: {lesson.title()} ")
#display_message('работа с функциями')

#def favourite_book(title):
 #   """Вывод сообщения"""
  #  print(f"Одна из моих любимых книг - {title}.")
#favourite_book("Алиса в стране чудес")

# #def make_shirt(size,text):
#   """Выводит информацию с размером футболки и текстом на ней"""
#   print(f"{size},{text}")
# make_shirt("М","Я люблю Россию!")

# #def make_shirt(size="L",text="I love Python!"):
#    """Выводит информацию с размером футболки и текстом на ней"""
#    print(f"{size},{text}")
# make_shirt()
# make_shirt("size","I love Russia")

# #def describe_city(town, country="Russia"):
#     """Выводит название города и страны, где он находится"""
#     print(f"{town.title()} is in {country.title()}")
# describe_city("Moscow")
# describe_city("Orel")
# describe_city("new York", "USA")

# #def build_person(first_name,last_name,age=None):
#     """Выводит информацию о человеке"""
#     person={'first':first_name,'last':last_name}
#     if age:
#         person['age']=age
#         return person
# musician=build_person('jimi','hendrics',age=27)
# print(musician)

# #def get_formated_name(first_name,last_name):
#     """Возвращает аккуратное написание имени"""
#     full_name=f"{first_name} {last_name}"
#     return full_name.title()
# while True:
#     print("\nPlease tell me your name: ")
#     print('(enter "q" at any time to quit)')
#
#     f_name=input("first name: ")
#     if f_name=="q":
#         break
#     l_name=input("last name: ")
#     if l_name == "q":
#         break
#
#     formated_name=get_formated_name(f_name,l_name)
#     print(f'\nHello,{formated_name}')
#

# #def c_towns(town,country):
#     """Выводит названия городов и стран"""
#     towns=f"{town}, {country}"
#     print(towns.title())
# c_towns("Минск","Беларусь")

# #def make_album(artist_name,album_name,treks=None):
#     """Вывод информации об артисте и его музыкальном альбоме"""
#     album={"artist":artist_name,"album_name":album_name}
#     if treks:
#         album["treks"]=treks
#     return album
# while True:
#     print("Введите данные по музыкальному альбому: ")
#     print('(enter "q" at any time to quit)')
#
#     artist=input("artist_name: ")
#     if artist == "q":
#         break
#
#     album_name=input("album: ")
#     if album_name == "q":
#         break
#
#     traks = input("treks: ")
#     if traks == "q":
#         break
#
#     artist_album=make_album(artist.title(),album_name.title(),traks)
#     print(f"{artist_album}")
#
#

# Программа, которая получает от пользователя список моделей дл 3Д печати и по мере готовности заказа,
# выводит список уже напечатанных моделей.
#
# #def print_models(unprinted_designs,completed_models):
#     """Иммитирует печать моделей, пока список не станет пустым.
#     Каждая модель после печати перемещается в список completed_models"""
#
#     while unprinted_designs:
#         current_design=unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)
# def show_completed_models(completed_models):
#     """Выводит информацию обо всех напечатанных моделях"""
#     print('\nThe following models have been printed:')
#     for completed_model in completed_models:
#         print(completed_model)
#
# unprinted_designs=['A','B','C']
# completed_models=[]
#
# print_models(unprinted_designs,completed_models)
# show_completed_models(completed_models)


# Задача: создать список коротких сообщений и передать его функции для вывода на экран.
# #def show_messages(messages):
#     """Выводит на экран все сообщения из списка"""
#     for message in messages:
#      print(f"\n{message.title()}")
#
# messages=['Hello!', 'good!', 'o my god!']
# show_messages(messages)

# #def send_messages(messages,sent_messages):
#     """Выводит на экран все сообщения из списка"""
#     while messages:
#         current_message=messages.pop()
#         print(current_message.title())
#         sent_messages.append(current_message)
# messages=['Hello!', 'good!', 'o my god!']
# sent_messages=[]
#
# send_messages(messages[:],sent_messages)
# print(messages)
# print(sent_messages)

# #def make_sandwich(size, *toppings):
#     """displays the composition of the sandwich"""
#     print(f"Making a {size}-inch sandwich with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")
#
# make_sandwich('smal','ham','salad')
# make_sandwich('big','cheese','ham','tomato')

# #def build_profile(first,last,**user_info):
#     """Build profile with user_info"""
#     user_info['first_name']=first
#     user_info['last_name']=last
#     return user_info
#
# user_profile=build_profile('Bob','Miller',age='27', location='Boston')
# print(user_profile)

def car_info(maker,name,**description):
    """displays info about cars"""
    print(f"info about this car:")
    description['maker']=maker
    description['name']=name
    return description

car=car_info('Lada','Lada_Vesta', color='red',year_of_production='2022')
print(car)



