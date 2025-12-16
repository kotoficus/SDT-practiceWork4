import unittest
import circle


class CircleTestCases(unittest.TestCase):
    """
    Тесты для функций area и perimeter из модуля circle.py
    """

    # Тесты для функции area(r)
    def test_area_normal_values(self):
        self.assertEquals(circle.area(2), 12.566370614359172)
        self.assertEquals(circle.area(5), 78.53981633974483)
        self.assertEquals(circle.area(7), 153.93804002589985)
        self.assertEquals(circle.area(10), 314.1592653589793)
        self.assertEquals(circle.area(12), 452.3893421169302)

    def test_area_zero_value(self):
        self.assertEquals(circle.area(0), 0)

    def test_area_big_values(self):
        self.assertEquals(circle.area(42), 5541.769440932396)
        self.assertEquals(circle.area(103), 33329.156461934115)
        self.assertEquals(circle.area(1007), 3185728.888780076)

    # Тесты для функции perimeter(r)
    def test_perimeter_normal_values(self):
        self.assertEquals(circle.perimeter(2), 12.566370614359172)
        self.assertEquals(circle.perimeter(5), 31.41592653589793)
        self.assertEquals(circle.perimeter(7), 43.982297150257104)
        self.assertEquals(circle.perimeter(10), 62.83185307179586)
        self.assertEquals(circle.perimeter(12), 75.39822368615503)

    def test_perimeter_zero_value(self):
        self.assertEquals(circle.perimeter(0), 0)

    def test_perimeter_big_values(self):
        self.assertEquals(circle.perimeter(42), 263.89378290154264)
        self.assertEquals(circle.perimeter(103), 647.1680866394973)
        self.assertEquals(circle.perimeter(1007), 6327.167604329843)
