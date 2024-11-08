import unittest

class TestSquared(unittest.TestCase):
    
    def test_negative(self):
        self.assertEqual((-3) ** 2, 9)