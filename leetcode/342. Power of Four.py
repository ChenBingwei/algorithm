# Given an integer n, return true if it is a power of four. Otherwise, return false.
#
# An integer n is a power of four, if there exists an integer x such that n == 4^x.
#
# Example 1:
# 
# Input: n = 16
# Output: true
# Example 2:
# 
# Input: n = 5
# Output: false
# Example 3:
# 
# Input: n = 1
# Output: true
# 
# 
# Constraints:
# 
# -231 <= n <= 231 - 1

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # return n > 0 and n & (n - 1) == 0 and n & 0xaaaaaaaa == 0
        return n > 0 and n & (n - 1) == 0 and n % 3 == 1


if __name__ == '__main__':
    a = Solution()
    print(a.isPowerOfFour(16))
