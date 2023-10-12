import unittest

from main import Solution


class BuildArrayFromPermutation(unittest.TestCase):
    def test_build_array_from_smallest_permutation(self):
        array = Solution().build_array_from([0])
        self.assertEqual([0], array)

    def test_build_array_from_size_two_permutation(self):
        array = Solution().build_array_from([1, 0])
        self.assertEqual([0, 1], array)

if __name__ == '__main__':
    unittest.main()
