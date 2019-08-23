import unittest


from listutil import unique


class FractionTest(unittest.TestCase):
    def test_unique_list(self):
        self.assertEqual([1, 3, 6, 5, 4], unique([1, 1, 1, 1, 3, 6, 5, 5, 5, 5, 4]))
        self.assertEqual(['a', 'b', 'c'], unique(['a', 'b', 'b', 'b', 'b', 'c']))
        self.assertEqual([[1, 3, 2], 2, 'b', 'c', 'f'], unique([[1, 3, 2], 2, 'b', 'c', [1, 3, 2], 'f', 'c', 2]))
        self.assertEqual([], unique([]))
        self.assertEqual([True, False], unique([True, False, True, True, False]))
