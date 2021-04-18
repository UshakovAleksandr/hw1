from main import Circle


def test_circle_create(create_circle):
    assert isinstance(create_circle, Circle)


def test_circle_perimeter(create_circle):
    assert round(create_circle.perimeter, 2) == 62.83


def test_circle_area(create_circle):
    assert round(create_circle.area, 2) == 314.16


def test_circle_add_area(create_circle, create_square):
    assert round(create_circle.add_area(create_square), 2) == 414.16
