# 16.9.1 Создайте класс любых геометрических фигур, где на выход мы получаем характеристики фигуры.

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Ст. тр-ка: a = {self.a}, b = {self.b}, c = {self.c}'


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'Ст. пр-ка: a = {self.a}, b = {self.b}'


triangle_1 = Triangle(10, 5, 12)
rectangle_1 = Rectangle(10, 15)

print(str(triangle_1))
print(str(rectangle_1))


# Создайте класс «прямоугольник» с помощью метода  __init__() 16.9.2

class Rectangle():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rectangle_area(self):
        return self.x * self.y


newRectangle = Rectangle(15, 8)
print(newRectangle.rectangle_area())


# Вам # нужно написать программу, обрабатывающую данные, и на выходе в консоль получить следующее:
# Клиент "Иван Петров". Баланс: 50 руб. 16.9.3

class Client:
    def __init__(self, name, balans):
        self.name = name
        self.balans = balans

    def get_info(self):
        return f"Клиент: {self.name}, Баланс:{self.balans},руб."


n1 = Client("Иван Петров", 50)
print(n1.get_info())


# Команда проекта «Дом питомца» планирует большой корпоратив для своих волонтеров.
# Вам необходимо написать программу, которая позволяла бы составлять список нескольких гостей.
# Решите задачу с помощью метода конструктора и примените один из принципов наследования.16.9.4
# При выводе в консоль вы должны получить:  “Иван Петров, г.Москва, статус "Наставник"

class Volunteer:
    def __init__(self, name, city):
        self.name = name
        self.city = city


class InvitedPersons(Volunteer):
    def __init__(self, name, city, status):
        super().__init__(name, city)
        self.status = status

    def __str__(self):
        return f'{self.name}, г.{self.city}, статус: {self.status}'


n1 = InvitedPersons('Иванов Иван Иванович', 'Москва', 'Наставник')
n2 = InvitedPersons('Сорокин Сергей Викторович', 'Мирный', 'Стажёр')
n3 = InvitedPersons('Петров Олег Николаевич', 'Ростов', 'Волонтёр')

print(n1)
print(n2)
print(n3)
