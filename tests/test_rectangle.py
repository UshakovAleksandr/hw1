from main import Rectangle


def test_rectangle_create(create_rectangle):
    assert isinstance(create_rectangle, Rectangle)


def test_rectangle_perimeter(create_rectangle):
    assert create_rectangle.perimeter == 60


def test_rectangle_area(create_rectangle):
    assert round(create_rectangle.area, 2) == 200


def test_rectangle_add_area(create_rectangle, create_triangle):
    assert round(create_rectangle.add_area(create_triangle), 2) == 243.30
