import unittest

from pydsalg.datastruct.hashset import HashSetString

class TestHashSet(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        min_value_len = 1
        max_value_len = 8
        hashset_len = 150
        cls.input0 = list(range(20))

    def test_00(self):
        hs = HashSetString()
        values = ['aaa', 'bbb', 'aaa', 'bbb', 'bbb', 'ccc', 'ddd', 'ddd']
        for val in values:
            self.assertFalse(val in hs)
            self.assertRaises(KeyError, lambda: hs.remove(val))
        for val in values:
            hs.add(val)

        for val in values:
            self.assertTrue(val in hs)

        self.assertEqual(len(hs), 4)

        hs.remove('aaa')
        self.assertEqual(len(hs), 3)
        self.assertRaises(KeyError, lambda: hs.remove('aaa'))
        hs.remove('bbb')
        self.assertEqual(len(hs), 2)
        self.assertTrue(hs)
        hs.remove('ccc')
        self.assertEqual(len(hs), 1)
        hs.remove('ddd')
        self.assertFalse(hs)
        self.assertEqual(len(hs), 0)

        for val in hs:
            print(val)


if __name__ == '__main__':
    unittest.main()
