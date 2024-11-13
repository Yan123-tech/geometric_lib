def area(a, h):
    if a < 0 or h < 0:
        raise ValueError("Base and height cannot be negative")
    return a * h / 2


def perimeter(a, b, c):
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Sides cannot be negative")
    return a + b + c
   