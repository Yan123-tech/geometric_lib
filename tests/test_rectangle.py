import unittest
import rectangle


class TestRectangle(unittest.TestCase):
    def test_area_positive(self):
        # Arrange
        a, b = 4, 5
        expected = a * b

        # Act
        result = rectangle.area(a, b)

        # Assert
        self.assertEqual(result, expected)

    def test_perimeter_positive(self):
        # Arrange
        a, b = 4, 5
        expected = 2 * (a + b)

        # Act
        result = rectangle.perimeter(a, b)

        # Assert
        self.assertEqual(result, expected)

    def test_area_negative(self):
        # Arrange
        a, b = -4, 5

        # Act & Assert
        with self.assertRaises(ValueError):
            rectangle.area(a, b)

    def test_perimeter_negative(self):
        # Arrange
        a, b = 4, -5

        # Act & Assert
        with self.assertRaises(ValueError):
            rectangle.perimeter(a, b)
