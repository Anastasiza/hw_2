import pytest

from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle
from src.Circle import Circle


@pytest.mark.parametrize(("side_a", "side_b", "area"),
                         [(4,5,20),
                         (7.5, 3.25, 24.375)])
def test_get_area_rectangle(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.get_area() == area

@pytest.mark.parametrize(("side_a", "side_b", "perimetr"),
                         [(4,5,18),
                         (7.5, 3.25, 21.50)])
def test_get_perimetr_rectangle(side_a, side_b, perimetr):
    r = Rectangle(side_a, side_b)
    assert  r.get_perimeter() == perimetr


@pytest.mark.parametrize(("side_a", "area"),
                         [(5,25),
                         (7.5, 56.25)])
def test_get_area_square(side_a, area):
    s = Square(side_a)
    assert s.get_area() == area


@pytest.mark.parametrize(("side_a", "perimetr"),
                         [(5, 20),
                         (7.5, 30)])
def test_get_perimetr_square(side_a, perimetr):
    s = Square(side_a)
    assert s.get_perimeter() == perimetr


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area"),
                         [(8, 6, 9, 23),
                         (7.5, 9.25, 6.77, 25)])
def test_get_area_triangle(side_a, side_b, side_c, area):
    t = Triangle(side_a, side_b, side_c)
    assert int(t.get_area()) == area

@pytest.mark.parametrize(("side_a", "side_b", "side_c", "perimetr"),
                         [(8, 6, 9, 23),
                         (7.5, 9.25, 6.77, 23.52)])
def test_get_perimetr_triangle(side_a, side_b, side_c, perimetr):
    t = Triangle(side_a, side_b, side_c)
    assert t.get_perimeter() == perimetr

@pytest.mark.parametrize(("radius", "area"),
                         [(7, 153),
                         (7.5, 176)])
def test_get_area_circle(radius, area):
    c = Circle(radius)
    assert int(c.get_area()) == area


@pytest.mark.parametrize(("radius", "perimetr"),
                         [(7, 43),
                         (4.5, 28)])
def test_get_perimetr_circle(radius, perimetr):
    c = Circle(radius)
    assert int(c.get_perimeter()) == perimetr