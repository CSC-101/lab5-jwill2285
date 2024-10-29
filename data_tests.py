import data
import unittest


class TestCases(unittest.TestCase):
    #### Time tests
    def test_Time_1(self):
        time = data.Time(7, 20, 1)
        self.assertEqual(7, time.hour)
        self.assertEqual(20, time.minute)
        self.assertEqual(1, time.second)


    def test_Time_2(self):
        time = data.Time(4, 19, 45)
        self.assertEqual(4, time.hour)
        self.assertEqual(19, time.minute)
        self.assertEqual(45, time.second)

    #### Add tests for Time.__eq__
    def test_Time_eq(self):
        input1 = data.Time(9,10,11)
        input2 = data.Time(9,10,11)
        self.assertEqual(input1,input2)
    def test_Time_eq_2(self):
        input1 = data.Time(4,19,45)
        input2 = data.Time(5,19,45)
        self.assertNotEqual(input1,input2)
    def test_Time_repr(self):
        input = data.Time(10,20,30)
        expected = "The Current Time is: 10:20:30"
        result = repr(input)
        self.assertEqual(expected,result)
    def test_Time_repr_2(self):
        input = data.Time(3,3,3)
        expected = "The Current Time is: 3:3:3"
        result = repr(input)
        self.assertEqual(expected,result)
    #### Add tests for Time.__repr__

    #### Point tests
    def test_Point_1(self):
        point = data.Point(7, 20)
        self.assertAlmostEqual(7, point.x)
        self.assertAlmostEqual(20, point.y)


    def test_Point_2(self):
        point = data.Point(4, 19)
        self.assertAlmostEqual(4, point.x)
        self.assertAlmostEqual(19, point.y)


    def test_Point_eq_1(self):
        point1 = data.Point(1, 20)
        point2 = data.Point(1, 20)
        self.assertEqual(point1, point2)


    def test_Point_eq_2(self):
        point1 = data.Point(1, 20)
        self.assertEqual(point1, point1)


    def test_Point_eq_3(self):
        point1 = data.Point(1, 20)
        point2 = data.Point(2, 20)
        self.assertNotEqual(point1, point2)


    def test_Point_eq_4(self):
        point = data.Point(1, 20)
        other = 1.20
        self.assertNotEqual(point, other)


    def test_Point_repr(self):
        point = data.Point(5, 75)
        self.assertEqual('Point(5, 75)', repr(point))


if __name__ == '__main__':
    unittest.main()
