# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def data_user(name, surname, b_year, city, email, phone):
    print(f'Имя - {name}; Фамилия - {surname}; Год Рождения - {b_year}; Город проживания - {city}; E-mail - {email}; Телефон - {phone}')

data_user(name=input("Введите имя:"),
          surname=input("Введите фамилию:"),
          b_year=input("Введите год рождения:"),
          city=input("Введите город проживания:"),
          email=input("Введите e-mail:"),
          phone=input("Введите телефон:"))


