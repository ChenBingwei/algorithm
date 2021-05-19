# You are given a 2D matrix of size m x n, consisting of non-negative integers.
# You are also given an integer k.
# 
# The value of coordinate (a, b) of the matrix is the XOR of all matrix[i][j]
# where 0 <= i <= a < m and 0 <= j <= b < n (0-indexed).
# 
# Find the kth largest value (1-indexed) of all the coordinates of matrix.
# 
#  
# 
# Example 1:
# 
# Input: matrix = [[5,2],[1,6]], k = 1
# Output: 7
# Explanation: The value of coordinate (0,1) is 5 XOR 2 = 7, which is the largest value.

# Example 2:
# 
# Input: matrix = [[5,2],[1,6]], k = 2
# Output: 5
# Explanation: The value of coordinate (0,0) is 5 = 5, which is the 2nd largest value.

# Example 3:
# 
# Input: matrix = [[5,2],[1,6]], k = 3
# Output: 4
# Explanation: The value of coordinate (1,0) is 5 XOR 1 = 4, which is the 3rd largest value.

# Example 4:
# 
# Input: matrix = [[5,2],[1,6]], k = 4
# Output: 0
# Explanation: The value of coordinate (1,1) is 5 XOR 2 XOR 1 XOR 6 = 0, which is the 4th largest value.
#  
# 
# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 1000
# 0 <= matrix[i][j] <= 106
# 1 <= k <= m * n
import operator
import random
from typing import List, Callable


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        new_matrix = [[0] * (n + 1) for _ in range(m + 1)]
        res_list = []
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                new_matrix[i][j] = new_matrix[i - 1][j] ^ new_matrix[i][j - 1] ^ new_matrix[i - 1][j - 1] ^ \
                                   matrix[i - 1][j - 1]
                res_list.append(new_matrix[i][j])
        res_list.sort(reverse=True)
        return res_list[k - 1]

    # 二维前缀和 + 快速选择算法
    def kthLargestValue_better(self, matrix: List[List[int]], k:int) -> int:
        m, n = len(matrix), len(matrix[0])
        pre = [[0] * (n + 1) for _ in range(m + 1)]
        results = list()
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pre[i][j] = pre[i - 1][j] ^ pre[i][j - 1] ^ pre[i - 1][j - 1] ^ matrix[i - 1][j - 1]
                results.append(pre[i][j])

        def nth_element(left: int, kth: int, right: int, op: Callable[[int, int], bool]):
            if left == right:
                return

            pivot = random.randint(left, right)
            results[pivot], results[right] = results[right], results[pivot]

            # 三路划分（three-way partition）
            sepl = sepr = left - 1
            for i in range(left, right + 1):
                if op(results[i], results[right]):
                    sepr += 1
                    if sepr != i:
                        results[sepr], results[i] = results[i], results[sepr]
                    sepl += 1
                    if sepl != sepr:
                        results[sepl], results[sepr] = results[sepr], results[sepl]
                elif results[i] == results[right]:
                    sepr += 1
                    if sepr != i:
                        results[sepr], results[i] = results[i], results[sepr]

            if sepl < left + kth <= sepr:
                return
            elif left + kth <= sepl:
                nth_element(left, kth, sepl, op)
            else:
                nth_element(sepr + 1, kth - (sepr - left + 1), right, op)

        nth_element(0, k - 1, len(results) - 1, operator.gt)
        return results[k - 1]

if __name__ == '__main__':
    a = Solution()
    print(a.kthLargestValue_better([[5,2],[1,6]], 2))

