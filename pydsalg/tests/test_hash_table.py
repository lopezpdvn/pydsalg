import unittest
from pprint import pprint

from pydsalg.hash_table import (HashTable0)

class TestHashTable0(unittest.TestCase):
    def test_misc_00(self):
        ht0 = HashTable0()
        self.assertRaises(KeyError, lambda: ht0['x'])
        self.assertEqual(ht0.length, HashTable0._ARR_DEFAULT_LENGTH)
        self.assertEqual(ht0.count, 0)

        ht0["670ag;bn's"] = 'value00'
        ht0["njdfg789d"] = 'value01'
        ht0["z76g6234"] = 'value02'

if __name__ == '__main__':
    unittest.main()
