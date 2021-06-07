# You are given an integer array nums and an integer target.
# 
# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums
# and then concatenate all the integers.
# 
# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the
# expression "+2-1". Return the number of different expressions that you can build, which evaluates to target.
# 
# 
# 
# Example 1:
# 
# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
# Example 2:
# 
# Input: nums = [1], target = 1
# Output: 1
# 
# 
# Constraints:
# 
# 1 <= nums.length <= 20
# 0 <= nums[i] <= 1000
# 0 <= sum(nums[i]) <= 1000
# -1000 <= target <= 1000
#
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        nums_sum = sum(nums)
        diff = nums_sum - target
        if diff < 0 or diff % 2 != 0:
            return 0
        nums_length = len(nums)
        neg = int(diff / 2)
        # dp = [[0] * (nums_length+1) for _ in range(neg+1)]
        dp = [[0] * (neg + 1) for _ in range(nums_length + 1)]
        dp[0][0] = 1
        for i in range(1, nums_length + 1):
            num = nums[i - 1]
            for j in range(neg + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= num:
                    dp[i][j] += dp[i - 1][j - num]
        return dp[nums_length][neg]

if __name__ == '__main__':
    a = Solution()
    print(a.findTargetSumWays([1,1,1,1,1], 3))