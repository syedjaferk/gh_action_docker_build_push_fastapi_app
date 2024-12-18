import unittest
from random_id_generator.id_generator import IdGenerator


class RandomIdGeneratorUnittest(unittest.TestCase):

    def test_get_random_id(self):
        id_gen = IdGenerator()
        result = id_gen.get_random_id()
        self.assertTrue(result)
