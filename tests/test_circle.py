import unittest
import circle
import math


class TestCircle(unittest.TestCase):
    def test_area_positive(self):
        # Arrange
        radius = 3
        expected = math.pi * radius ** 2

        # Act
        result = circle.area(radius)

        # Assert
        self.assertAlmostEqual(result, expected)

    def test_perimeter_positive(self):
        # Arrange
        radius = 3
        expected = 2 * math.pi * radius

        # Act
        result = circle.perimeter(radius)

        # Assert
        self.assertAlmostEqual(result, expected)

    def test_area_negative(self):
        # Arrange
        radius = -3

        # Act & Assert
        with self.assertRaises(ValueError):
            circle.area(radius)

    def test_perimeter_negative(self):
        # Arrange
        radius = -3

        # Act & Assert
        with self.assertRaises(ValueError):
            circle.perimeter(radius)
