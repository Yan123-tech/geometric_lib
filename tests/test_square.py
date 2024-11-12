import unittest
import square

class TestSquare(unittest.TestCase):
    def test_area_positive(self):
        # Arrange
        side = 4
        expected = side ** 2

        # Act
        result = square.area(side)

        # Assert
        self.assertEqual(result, expected)

    def test_perimeter_positive(self):
        # Arrange
        side = 4
        expected = 4 * side

        # Act
        result = square.perimeter(side)

        # Assert
        self.assertEqual(result, expected)

    def test_area_negative(self):
        # Arrange
        side = -4

        # Act & Assert
        with self.assertRaises(ValueError):
            square.area(side)

    def test_perimeter_negative(self):
        # Arrange
        side = -4

        # Act & Assert
        with self.assertRaises(ValueError):
            square.perimeter(side)