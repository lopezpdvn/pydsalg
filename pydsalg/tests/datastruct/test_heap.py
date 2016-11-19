import unittest
from pprint import pprint
from random import randint

from pysyspol.util import random_alphanumeric_str

from pydsalg.datastruct.heap import heap_sort

class TestHeap(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sorted_big = [000, 111, 222, 333, 444, 555, 666,777, 888, 999]
        sorted_two = [222, 888]
        sorted_one = [999]
        sorted_three = [000, 333, 999]
        sorted_four = [111, 444, 555, 666]
        sorted_empty = []
        cls.sorted_arrs = [sorted_one, sorted_two, sorted_three, sorted_four,
                sorted_big, sorted_empty]

    def setUp(self):
        unsorted_big = [888, 222, 333, 000, 999, 777, 555, 111, 666, 444]
        unsorted_two = [888, 222]
        unsorted_one = [999]
        unsorted_three = [333, 000, 999]
        unsorted_four = [555, 111, 666, 444]
        unsorted_empty = []
        self.unsorted_arrs = [unsorted_one, unsorted_two, unsorted_three,
                unsorted_four, unsorted_big, unsorted_empty]

    def test_heap_sort(self):
        for u, s in zip(self.unsorted_arrs, self.sorted_arrs):
            heap_sort(u)
            self.assertEqual(u, s)

if __name__ == '__main__':
    unittest.main()
