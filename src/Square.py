from src.Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a):
        if side_a <= 0:
            ValueError("Сторона квадрата должна быть больше 0 ")
        super().__init__(side_a, side_a)
        self.name = "Square"
        self.side_a = side_a


