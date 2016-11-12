import unittest
from pprint import pprint
from random import randint

from pysyspol.util import random_alphanumeric_str

from pydsalg.hash_table import (HashTable0)

class TestHashTable0(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        min_key_len = 8
        max_key_len = 16
        min_value_len = 1
        max_value_len = 8
        testdict0_len = 150
        cls.testdict0 = {}

        for i in range(testdict0_len):
            key_len = randint(min_key_len, max_key_len)
            value_len = randint(min_value_len, max_value_len)
            key = random_alphanumeric_str(key_len)
            value = random_alphanumeric_str(value_len)
            cls.testdict0[key] = value

    def test_misc_00(self):
        ht0 = HashTable0()
        self.assertRaises(KeyError, lambda: ht0['x'])
        self.assertEqual(ht0.length, HashTable0._ARR_DEFAULT_LENGTH)
        self.assertEqual(ht0.count, 0)

        ht0["670ag;bn's"] = 'value00'
        ht0["njdfg789d"] = 'value01'
        ht0["z76g6234"] = 'value02'

        self.assertEqual(ht0.count, 3)

    def test_misc_01(self):
        ht0 = HashTable0()

        for k, v in self.testdict0.items():
            ht0[k] = v

        self.assertEqual(ht0.count, len(self.testdict0))

        for k, v in self.testdict0.items():
            ht0[k] = v

    def test_membership(self):
        ht0 = HashTable0()

        for k in self.testdict0:
            self.assertTrue(k not in ht0)

        for k, v in self.testdict0.items():
            ht0[k] = v

        for k in self.testdict0:
            self.assertTrue(k in ht0)

if __name__ == '__main__':
    unittest.main()
