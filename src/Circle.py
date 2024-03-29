from math import pi

from src.Figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            ValueError("Радиус должен быть больше 0 ")
        super().__init__(name="Circle")
        self.__radius = radius

    def get_area(self):
        return pi * self.__radius ** 2

    def get_perimeter(self):
        return 2 * pi * self.__radius
