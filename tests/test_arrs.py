import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([1, 2, 3], 5, "test"), "test")
        self.assertEqual(arrs.get([], 0, "test"), "test")
        self.assertIsNone(arrs.get([], -1))
        self.assertEqual(arrs.get([1, 2, 3], -1, "default"), "default")
        self.assertEqual(arrs.get([1, 2, 3], 3, "default"), "default")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 0, 2), [1, 2])
        self.assertEqual(arrs.my_slice([1, 2, 3], 0, 5), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], -2), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], -2, -1), [2])
        self.assertEqual(arrs.my_slice([], 0, 2), [])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1, 1), [])
    def test_get_default(self):
        self.assertEqual(arrs.get([1, 2, 3], 1), 2)
        self.assertEqual(arrs.get([1, 2, 3], 5), None)
        self.assertEqual(arrs.get([], 0), None)
