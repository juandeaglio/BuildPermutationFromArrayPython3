from typing import List

class Solution:
    def build_array_from(self, nums: List[int]) -> List[int]:
        array = [0] * len(nums)
        for i, val in enumerate(nums):
            array[i] = nums[val]

        return array

if __name__ == '__main__':
    pass
