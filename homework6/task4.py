# 4. Реализуйте базовый класс Car. 
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
# А также методы: go, stop, turn(direction), которые должны сообщать, 
# что машина поехала, остановилась, повернула (куда). 
# 
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
# 
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. 
# Для классов TownCar и WorkCar переопределите метод show_speed. 
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) 
# должно выводиться сообщение о превышении скорости.
# 
# Создайте экземпляры классов, передайте значения атрибутов. 
# Выполните доступ к атрибутам, выведите результат. 
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return "Машина поехала"
    def stop(self):
        return "Машина остановилась"
    def turn(self, direction):
        return "Машина повернула " + direction

    def show_speed(self):
        return self.speed

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Вы превысили скорость 60км/ч. Ваша скорость: {self.speed}км/ч')
        else:
            print(f'Ваша скорость: {self.speed}км/ч')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Вы превысили скорость 40км/ч. Ваша скорость: {self.speed}км/ч')
        else:
            print(f'Ваша скорость: {self.speed}км/ч')

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)

uaz = Car(100, "green", "УАЗ")
ferrari = SportCar(200, "red", "Ferrari")
ford = TownCar(70, "white", "Ford Focus")
toyota = WorkCar(50, "black", "Toyota Corolla")
police = PoliceCar(150, "silver", "Renault Logan 2")

for car in [uaz, ferrari, ford, toyota, police]:
    print(f'Car Name: {car.name}')
    print(f'Speed: {car.speed}')
    print(f'Color: {car.color}')
    print(f'Is Polce: {car.is_police}')
    print(f'Overspeeding: {car.show_speed()}')
    print(f'Go message: {car.go()}')
    print(f'Stop message: {car.stop()}')
    print(f'Turn left message: {car.turn("налево")}')
    print(f'Turn right message: {car.turn("направо")}')
    print('============')
