import unittest

from main import build_array_from


class BuildArrayFromPermutation(unittest.TestCase):
    def test_build_array_from_smallest_permutation(self):
        array = build_array_from([0])
        self.assertEqual([0], array)


if __name__ == '__main__':
    unittest.main()
