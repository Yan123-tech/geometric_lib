import unittest
from calculate import calc

class TestCalculate(unittest.TestCase):
    def test_calc_circle_area(self):
        # Arrange
        fig, func, size = "circle", "area", [3]

        # Act
        result = calc(fig, func, size)

        # Assert
        self.assertIsNotNone(result)

    def test_calc_square_perimeter(self):
        # Arrange
        fig, func, size = "square", "perimeter", [4]

        # Act
        result = calc(fig, func, size)

        # Assert
        self.assertIsNotNone(result)

    def test_calc_invalid_figure(self):
        # Arrange
        fig = "pentagon"
        func = "area"
        size = [3]
        
        # Act & Assert
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_calc_invalid_function(self):
        # Arrange
        fig, func, size = "circle", "volume", [3]

        # Act & Assert
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_calc_invalid_size(self):
        # Arrange
        fig = "circle"
        func = "volume"  
        size = [-4]

        # Act & Assert
        with self.assertRaises(ValueError):
            calc(fig, func, size)