from main import Triangle


def test_triangle_create(create_triangle):
    assert isinstance(create_triangle, Triangle)


def test_triangle_perimeter(create_triangle):
    assert create_triangle.perimeter == 30


def test_triangle_area(create_triangle):
    assert round(create_triangle.area, 2) == 43.30


def test_triangle_add_area(create_triangle, create_rectangle):
    assert round(create_triangle.add_area(create_rectangle), 2) == 243.30
