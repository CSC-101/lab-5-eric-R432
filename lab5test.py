import data
import lab5
import unittest

from data import Point


# Write your test cases for each part below.

class TestCases(unittest.TestCase):

    # Part 3
    def test_time_add(self):

        time1 = data.Time(1, 30, 45)
        time2 = data.Time(2, 45, 30)
        expected = data.Time(4, 16, 15)
        result = lab5.time_add(time1, time2)
        self.assertEqual(result.hours, expected.hours)
        self.assertEqual(result.minutes, expected.minutes)
        self.assertEqual(result.seconds, expected.seconds)

    def test_time_add_2(self):
        time3 = data.Time(1, 30, 30)
        time4 = data.Time(0, 31, 50)
        expected = data.Time(2, 2, 20)
        result = lab5.time_add(time3, time4)
        self.assertEqual(result.hours, expected.hours)
        self.assertEqual(result.minutes, expected.minutes)
        self.assertEqual(result.seconds, expected.seconds)

    def test_is_descending(self):

        lst = [5.0, 4.0, 3.0, 2.0, 1.0]
        result = lab5.is_descending(lst)
        expected = True
        assert result == expected, f"Expected {expected}, got {result}"

    def test_is_descending_2(self):
        lst = [0.0, 7.0, 3.0, 2.0, 1.0]
        result = lab5.is_descending(lst)
        expected = False
        assert result == expected, f"Expected {expected}, got {result}"



    def test_largest_between(self):

        numbers = [1, 3, 5, 2, 4]
        result = lab5.largest_between(numbers, 1, 3)
        expected = 2
        assert result == expected, f"Expected {expected}, got {result}"

    def test_largest_between_2(self):
        numbers = []
        result = lab5.largest_between(numbers, 4, 0)
        expected = None
        assert result == expected, f"Expected {expected}, got {result}"


    def test_furthest_from_origin(self):

        points = [data.Point(1, 2), Point(3, 4), Point(-5, -6)]
        result = lab5.furthest_from_origin(points)
        expected = 2
        assert result == expected, f"Expected {expected}, got {result}"

    def test_furthest_from_orign_2(self):
        points = [data.Point(0, 0), Point(0, 0), Point(0, 0)]
        result = lab5.furthest_from_origin(points)
        expected = 0
        assert result == expected, f"Expected {expected}, got {result}"






if __name__ == '__main__':
    unittest.main()
