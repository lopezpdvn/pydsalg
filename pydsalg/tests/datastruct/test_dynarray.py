import unittest
from pprint import pprint
from random import randint

from pydsalg.datastruct.dynarray import DynamicArray

class TestDynamicArray(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.input0 = list(range(20))

    def test_00(self):
        dynarr = DynamicArray()
        input0 = self.input0.copy()
        dynarr.append(input0.pop(0))
        dynarr.append(input0.pop(0))
        dynarr.append(input0.pop(0))
        dynarr.append(input0.pop(0))
        dynarr.append(input0.pop(0))
        dynarr.append(input0.pop(0))
        dynarr.append(input0.pop(0))
        dynarr.append(input0.pop(0))
        dynarr.append(input0.pop(0))
        dynarr.append(input0.pop(0))
        print(dynarr._arr)
        print(dynarr.remove())
        print(dynarr.remove())
        print(dynarr.remove())
        print(dynarr.remove())
        print(dynarr.remove())
        print(dynarr.remove())
        print(dynarr.remove())
        print(dynarr.remove())
        print(dynarr.remove())
        print(dynarr.remove())
        for i in 'abcdefghijklmnopq':
            dynarr.append(i)

        print(dynarr._arr)

    def test_01(self):
        dynarr = DynamicArray(start=0)
        input0 = self.input0.copy()
        dynarr.append(input0.pop(0))
        dynarr.append(input0.pop(0))
        dynarr.append(input0.pop(0))
        dynarr.append(input0.pop(0))
        dynarr.append(input0.pop(0))
        dynarr.append(input0.pop(0))
        dynarr.append(input0.pop(0))
        dynarr.append(input0.pop(0))
        dynarr.append(input0.pop(0))
        dynarr.append(input0.pop(0))
        dynarr.append(input0.pop(0))
        dynarr.append(input0.pop(0))
        #print(dynarr._arr)

if __name__ == '__main__':
    unittest.main()
