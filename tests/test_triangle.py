import unittest
import triangle


class TestTriangle(unittest.TestCase):
    def test_area_positive(self):
        # Arrange
        base, height = 4, 5
        expected = base * height / 2

        # Act
        result = triangle.area(base, height)

        # Assert
        self.assertEqual(result, expected)

    def test_perimeter_positive(self):
        # Arrange
        a, b, c = 3, 4, 5
        expected = a + b + c

        # Act
        result = triangle.perimeter(a, b, c)

        # Assert
        self.assertEqual(result, expected)

    def test_area_negative(self):
        # Arrange
        base, height = -4, 5

        # Act & Assert
        with self.assertRaises(ValueError):
            triangle.area(base, height)

    def test_perimeter_negative(self):
        # Arrange
        a, b, c = 3, 4, -5

        # Act & Assert
        with self.assertRaises(ValueError):
            triangle.perimeter(a, b, c)
