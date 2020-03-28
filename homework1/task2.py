# 2. Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

print('Введите количество секунд: ')

seconds = int(input())
minutes = seconds // 60
hours = minutes // 60

seconds = seconds % 60
minutes = minutes % 60
hours = hours % 24

if seconds < 10:
  seconds = f'0{seconds}'
if minutes < 10:
  minutes = f'0{minutes}'
if hours < 10:
  hours = f'0{hours}'

print(f'Вы ввели время: {hours}:{minutes}:{seconds}')
