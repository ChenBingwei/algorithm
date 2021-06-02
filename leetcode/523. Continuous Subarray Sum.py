# Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two
# whose elements sum up to a multiple of k, or false otherwise.
# 
# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
# 
# 
# 
# Example 1:
# 
# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
# Example 2:
# 
# Input: nums = [23,2,6,4,7], k = 6
# Output: true
# Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
# 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
# Example 3:
# 
# Input: nums = [23,2,6,4,7], k = 13
# Output: false
# 
# 
# Constraints:
# 
# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109
# 0 <= sum(nums[i]) <= 231 - 1
# 1 <= k <= 231 - 1
from itertools import accumulate
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        new_nums = list(map(lambda x: x % k, accumulate(nums)))
        tmp_dict = {0: -1}
        for i, v in enumerate(new_nums):
            if v not in tmp_dict:
                tmp_dict[v] = i
            elif i - tmp_dict[v] >= 2:
                return True
        return False

    def checkSubarraySum_plus(self, nums: List[int], k: int) -> bool:
        tmp_dict = {0: -1}
        accumulate_sum = 0
        for i, v in enumerate(nums):
            accumulate_sum += v
            remainder = accumulate_sum % k
            if remainder not in tmp_dict:
                tmp_dict[remainder] = i
            elif i - tmp_dict[remainder] >= 2:
                return True
        return False


if __name__ == '__main__':
    a = Solution()
    print(a.checkSubarraySum([7, 23, 2, 4, 10, 6], 7))
