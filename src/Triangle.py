from src.Figure import Figure
from math import sqrt

class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <=0 or side_c:
            ValueError("Сторона треугольника должна быть больше 0")
        elif side_a + side_b < side_c or side_a + side_c < side_b or side_b + side_c < side_a:
            ValueError("Такой треугольник невозможно создать")

        super().__init__(name="Triangle")
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c

    def get_area(self):
        pp = self.get_perimeter() / 2
        return (sqrt(pp * (pp - self.__side_a) * (pp - self.__side_b) * (pp - self.__side_c)))

    def get_perimeter(self):
        return self.__side_a + self.__side_b + self.__side_c