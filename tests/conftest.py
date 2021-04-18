import pytest
from main import Triangle, Rectangle, Square, Circle


@pytest.fixture
def create_triangle():
    triangle = Triangle("triangle", 3, 10, 10, 10)
    return triangle


@pytest.fixture
def create_rectangle():
    rectangle = Rectangle("rectangle", 3, 10, 20)
    return rectangle


@pytest.fixture
def create_square():
    square = Square("square", 3, 10)
    return square


@pytest.fixture
def create_circle():
    circle = Circle("circle", 0, 10)
    return circle
