import unittest
import square


class SquareTestCases(unittest.TestCase):
   """
   Тесты для функций area и perimeter из модуля square.py
   """


   # Тесты для функции area(r)
   def test_area_normal_values(self):
       self.assertEquals(square.area(2), 4)
       self.assertEquals(square.area(5), 25)
       self.assertEquals(square.area(7), 49)
       self.assertEquals(square.area(10), 100)
       self.assertEquals(square.area(12), 144)


   def test_area_zero_value(self):
       self.assertEquals(square.area(0), 0)


   def test_area_big_values(self):
       self.assertEquals(square.area(42), 1764)
       self.assertEquals(square.area(103), 10609)
       self.assertEquals(square.area(1007), 1014049)


   # Тесты для функции perimeter(r)
   def test_perimeter_normal_values(self):
       self.assertEquals(square.perimeter(2), 8)
       self.assertEquals(square.perimeter(5), 20)
       self.assertEquals(square.perimeter(7), 28)
       self.assertEquals(square.perimeter(10), 40)
       self.assertEquals(square.perimeter(12), 48)


   def test_perimeter_zero_value(self):
       self.assertEquals(square.perimeter(0), 0)


   def test_perimeter_big_values(self):
       self.assertEquals(square.perimeter(42), 168)
       self.assertEquals(square.perimeter(103), 412)
       self.assertEquals(square.perimeter(1007), 4028)
