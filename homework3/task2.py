# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: 
# имя, фамилия, год рождения, город проживания, email, телефон. 
# Функция должна принимать параметры как именованные аргументы. 
# Реализовать вывод данных о пользователе одной строкой.

def print_users_data(firstname, lastname, birth_year, city, email, phone):
    print(f'имя: {firstname}, фамилия: {lastname}, год рождения: {birth_year}, город проживания: {city}, email: {email}, телефон: {phone}')

print_users_data(
    firstname="Thomas",
    lastname="Black",
    birth_year="1983",
    city="Moscow",
    email="cool@yandex.ru",
    phone="+79213127721"
)