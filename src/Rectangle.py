from src.Figure import Figure


class Rectangle(Figure):

    def __init__(self,side_a, side_b):
        super().__init__(name="Rectangle")
        if side_a <= 0 or side_b <=0:
            raise ValueError("Сторона прямоугольника должна быть больше нуля")
        self.__side_a = side_a
        self.__side_b = side_b


    def get_area(self):
        return self.__side_a * self.__side_b

    def get_perimeter(self):
        return (self.__side_a + self.__side_b) * 2
