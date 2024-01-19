import pytest

from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle
from src.Circle import Circle



@pytest.mark.parametrize(("side_a", "side_b", "area"),
                         [(-4,-5,-20),
                         (-7.5, -3.25, -24.375),
                          (0,5,20)])
def test_get_area_rectangle(side_a, side_b, area):
    with pytest.raises(ValueError):
        r = Rectangle(side_a, side_b)
        assert r.get_area() == area

@pytest.mark.parametrize(("side_a", "side_b", "perimetr"),
                         [(-4,-5,-18),
                         (-7.5, -3.25, -21.50),
                          (0,5,18)])
def test_get_perimetr_rectangle(side_a, side_b, perimetr):
    with pytest.raises(ValueError):
        r = Rectangle(side_a, side_b)
        assert  r.get_perimeter() == perimetr


@pytest.mark.parametrize(("side_a", "area"),
                         [(-5,-25),
                         (-7.5, -56.25),
                          ( 0, 0)])
def test_get_area_square(side_a, area):
    with pytest.raises(ValueError):
        s = Square(side_a)
        assert s.get_area() == area


@pytest.mark.parametrize(("side_a", "perimetr"),
                         [(-5, -20),
                         (-7.5, -30),
                          (0, 0)])
def test_get_perimetr_square(side_a, perimetr):
    with pytest.raises(ValueError):
        s = Square(side_a)
        assert s.get_perimeter() == perimetr


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area"),
                         [(-4, 6, 9, 23)])
def test_get_area_triangle(side_a, side_b, side_c, area):
    with pytest.raises(ValueError):
        t = Triangle(side_a, side_b, side_c)
        assert int(t.get_area()) == area

@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area"),
                         [(7, 2, 2, 6)])
def test_get_area_triangle(side_a, side_b, side_c, area):
    with pytest.raises(ValueError):
        t = Triangle(side_a, side_b, side_c)
        assert int(t.get_area()) == area

@pytest.mark.parametrize(("side_a", "side_b", "side_c", "perimetr"),
                         [(0, -6, -9, 15)
                         ])
def test_get_perimetr_triangle(side_a, side_b, side_c, perimetr):
    with pytest.raises(ValueError):
        t = Triangle(side_a, side_b, side_c)
        assert t.get_perimeter() == perimetr

@pytest.mark.parametrize(("radius", "area"),
                         [(-7, 153),
                         (0, 0)])
def test_get_area_circle(radius, area):
    with pytest.raises(ValueError):
        c = Circle(radius)
        assert int(c.get_area()) == area


@pytest.mark.parametrize(("radius", "perimetr"),
                         [(-7, 43),
                         (0, 28)])
def test_get_perimetr_circle(radius, perimetr):
    with pytest.raises(ValueError):
        c = Circle(radius)
        assert int(c.get_perimeter()) == perimetr
