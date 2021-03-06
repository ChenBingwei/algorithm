# You are given an array nums consisting of non-negative integers. You are also given a queries array, where queries[
# i] = [xi, mi].
# 
# The answer to the ith query is the maximum bitwise XOR value of xi and any element of nums that does not exceed mi.
# In other words, the answer is max(nums[j] XOR xi) for all j such that nums[j] <= mi. If all elements in nums are
# larger than mi, then the answer is -1.
# 
# Return an integer array answer where answer.length == queries.length and answer[i] is the answer to the ith query.
# 
#  
# 
# Example 1:
# 
# Input: nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
# Output: [3,3,7]
# Explanation:
# 1) 0 and 1 are the only two integers not greater than 1. 0 XOR 3 = 3 and 1 XOR 3 = 2. The larger of the two is 3.
# 2) 1 XOR 2 = 3.
# 3) 5 XOR 2 = 7.
# Example 2:
# 
# Input: nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]
# Output: [15,-1,5]
#  
# 
# Constraints:
# 
# 1 <= nums.length, queries.length <= 105
# queries[i].length == 2
# 0 <= nums[j], xi, mi <= 109
#
from typing import List


class Trie:
    L = 30

    def __init__(self):
        self.left = None
        self.right = None

    def insert(self, val: int):
        node = self
        for i in range(Trie.L, -1, -1):
            bit = (val >> i) & 1
            if bit == 0:
                if not node.left:
                    node.left = Trie()
                node = node.left
            else:
                if not node.right:
                    node.right = Trie()
                node = node.right

    def getMaxXor(self, val: int) -> int:
        ans, node = 0, self
        for i in range(Trie.L, -1, -1):
            bit = (val >> i) & 1
            check = False
            if bit == 0:
                if node.right:
                    node = node.right
                    check = True
                else:
                    node = node.left
            else:
                if node.left:
                    node = node.left
                    check = True
                else:
                    node = node.right
            if check:
                ans |= 1 << i
        return ans


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n, q = len(nums), len(queries)
        nums.sort()
        queries = sorted([(x, m, i) for i, (x, m) in enumerate(queries)], key=lambda query: query[1])

        ans = [0] * q
        t = Trie()
        idx = 0
        for x, m, qid in queries:
            while idx < n and nums[idx] <= m:
                t.insert(nums[idx])
                idx += 1
            if idx == 0:
                # 字典树为空
                ans[qid] = -1
            else:
                ans[qid] = t.getMaxXor(x)

        return ans

