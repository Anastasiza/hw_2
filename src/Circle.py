from math import pi


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            ValueError("Сторона треугольника должна быть больше 0")
        super().__init__(name="Circle")
        self.__radius = radius

    def get_area(self):
        return pi * self.__radius ** 2

    def get_perimeter(self):
        return 2 * pi * self.__radius
