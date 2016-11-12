import unittest

from pydsalg.hash_table import (dummy_function, DUMMY_GLOBAL_CONSTANT_0,
    DUMMY_GLOBAL_CONSTANT_1)

class TestDummies(unittest.TestCase):

  def test_global_variables(self):
      self.assertEqual(DUMMY_GLOBAL_CONSTANT_0, 'FOO')
      self.assertEqual(DUMMY_GLOBAL_CONSTANT_1, 'BAR')

  def test_dummy_funcion(self):
      self.assertEqual(dummy_function('a'), 'a');
      self.assertEqual(dummy_function(555), 555);

if __name__ == '__main__':
    unittest.main()
