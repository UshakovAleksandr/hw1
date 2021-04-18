from main import Square


def test_square_create(create_square):
    assert isinstance(create_square, Square)


def test_square_perimeter(create_square):
    assert create_square.perimeter == 40


def test_square_area(create_square):
    assert round(create_square.area, 2) == 100


def test_square_add_area(create_square, create_rectangle):
    assert round(create_square.add_area(create_rectangle), 2) == 300
