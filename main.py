import math


class Figure:

    def __init__(self, name, angles):
        self.name = name
        self.angles = angles

    @staticmethod
    def perimeter(figure, *args):
        if figure == "triangle":
            return sum(args)
        if figure == "rectangle":
            return 2 * sum(args)
        if figure == "square":
            return 4 * args[0]
        if figure == "circle":
            return 2 * math.pi * args[0]
        else:
            raise Exception("Incorrect Class")

    @staticmethod
    def area(figure, *args):
        if figure == "triangle":
            p = sum(args) / 2
            return math.sqrt(p * (p - args[0]) * (p - args[1]) * (p - args[2]))
        if figure == "rectangle":
            return args[0] * args[1]
        if figure == "square":
            return args[0] ** 2
        if figure == "circle":
            return math.pi * args[0] ** 2
        else:
            raise Exception("Incorrect Class")

    def add_area(self, figure):
        figures_lst = ["triangle", "rectangle", "square", "circle"]
        if figure.name in figures_lst:
            return self.area + figure.area
        else:
            raise Exception("Incorrect Class")


class Triangle(Figure):

    def __init__(self, name, angles, side1, side2, side3):
        super().__init__(name, angles)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.perimeter = Triangle.perimeter(self.name, self.side1, self.side2, self.side3)
        self.area = Triangle.area(self.name, self.side1, self.side2, self.side3)


class Rectangle(Figure):

    def __init__(self, name, angles, side1, side2):
        super().__init__(name, angles)
        self.side1 = side1
        self.side2 = side2
        self.perimeter = Rectangle.perimeter(self.name, self.side1, self.side2)
        self.area = Rectangle.area(self.name, self.side1, self.side2)


class Square(Figure):

    def __init__(self, name, angles, side1):
        super().__init__(name, angles)
        self.side1 = side1
        self.perimeter = Square.perimeter(self.name, self.side1)
        self.area = Square.area(self.name, self.side1)


class Circle(Figure):

    def __init__(self, name, angles, radius):
        super().__init__(name, angles)
        self.radius = radius
        self.perimeter = Figure.perimeter(self.name, self.radius)
        self.area = Figure.area(self.name, self.radius)


def main():
    triangle = Triangle("triangle", 3, 10, 10, 10)
    print(triangle.perimeter)
    print(triangle.area)
    rectangle = Rectangle("rectangle", 4, 10, 20)
    print(rectangle.perimeter)
    print(rectangle.area)
    print(rectangle.add_area(triangle))
    square = Square("square", 4, 10)
    print(square.perimeter)
    print(square.area)
    print(square.add_area(rectangle))
    circle = Circle("circle", 0, 10)
    print(circle.perimeter)
    print(circle.area)
    print(circle.add_area(square))


if __name__ == '__main__':
    main()
