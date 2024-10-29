import data
import lab5
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test_time_add(self):
        input1 = data.Time(3,40,20)
        input2 = data.Time(3,40,20)
        result = lab5.time_add(input1,input2)
        expected = "Hours: 7, Minutes: 20, Seconds: 40"
        self.assertEqual(expected,result)
    def test_time_add_2(self):
        input1 = data.Time(10,60,90)
        input2 = data.Time(10,60,30)
        result = lab5.time_add(input1,input2)
        expected = "Hours: 22, Minutes: 2, Seconds: 0"
        self.assertEqual(expected,result)
 # Part 4
    def test_is_descending(self):
        input = [5,4,3,2,1]
        result = lab5.is_descending(input)
        expected = True
        self.assertEqual(expected,result)
    def test_is_descending_2(self):
        input = [9,8,5,3,4]
        result = lab5.is_descending(input)
        expected = False
        self.assertEqual(expected,result)
    # Part 5
    def test_largest_between(self):
        input = ([1,2,9,3,8,4,7,6,5])
        second = 3
        third = 7
        result = lab5.largest_between(input,second,third)
        expected = 8
        self.assertEqual(expected,result)
    def test_largest_between_2(self):
        input = ([1,2,9,3,8,4,7,6,5])
        second = -5
        third = 10
        result = lab5.largest_between(input,second,third)
        expected = None
        self.assertEqual(expected,result)
    # Part 6
    def test_furthest_from_origin(self):
        input = [data.Point(1,2), data.Point(3,-4)]
        result = lab5.furthest_from_origin(input)
        expected = 1
        self.assertEqual(expected,result)
    def test_furthest_from_origin_2(self):
        input = []
        result = lab5.furthest_from_origin(input)
        expected = None
        self.assertEqual(expected,result)





if __name__ == '__main__':
    unittest.main()
