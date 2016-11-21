import unittest
from pprint import pprint
from random import randint

from pydsalg.datastruct.heap import heapsort0

class TestHeap(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sorted_big = [000, 111, 222, 333, 444, 555, 666,777, 888, 999]
        sorted_two = [222, 888]
        sorted_one = [999]
        sorted_three = [000, 333, 999]
        sorted_four = [111, 444, 555, 666]
        sorted_empty = []
        a = [1,2,3,4,5,6,7,8]
        cls.sorted_arrs = [sorted_one, sorted_two, sorted_three, sorted_four,
                sorted_big, sorted_empty, a]

    def setUp(self):
        unsorted_big = [888, 222, 333, 000, 999, 777, 555, 111, 666, 444]
        unsorted_two = [888, 222]
        unsorted_one = [999]
        unsorted_three = [333, 000, 999]
        unsorted_four = [555, 111, 666, 444]
        unsorted_empty = []
        a = [6,5,3,1,8,7,2,4]
        self.unsorted_arrs = [unsorted_one, unsorted_two, unsorted_three,
                unsorted_four, unsorted_big, unsorted_empty, a]

    def test_heapsort0_1(self):
        for u, s in zip(self.unsorted_arrs, self.sorted_arrs):
            heapsort0(u)
            self.assertEqual(u, s)

if __name__ == '__main__':
    unittest.main()
