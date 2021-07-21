# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
# 
# A subarray is a contiguous part of the array.
# 
# 
# 
# Example 1:
# 
# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
# Explanation: The 4 subarrays are bolded and underlined below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# Example 2:
# 
# Input: nums = [0,0,0,0,0], goal = 0
# Output: 15
# 
# 
# Constraints:
# 
# 1 <= nums.length <= 3 * 104
# nums[i] is either 0 or 1.
# 0 <= goal <= nums.length
#
from typing import List


class Solution:
    @staticmethod
    def numSubarraysWithSum(nums: List[int], goal: int) -> int:
        sums = 0
        res = 0
        presum_dict = {}
        for i in nums:
            presum_dict.setdefault(sums, 0)
            presum_dict[sums] += 1
            sums += 1
            if sums - goal in presum_dict:
                res += 1
        return res


if __name__ == '__main__':
    res = Solution.numSubarraysWithSum(nums=[1,0,1,0,1], goal=2)
    print(res)
