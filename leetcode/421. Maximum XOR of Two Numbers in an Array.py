# 给你一个整数数组 nums ，返回 nums[i] XOR nums[j] 的最大运算结果，其中 0 ≤ i ≤ j < n 。
#
# 进阶：你可以在 O(n) 的时间解决这个问题吗？
#
#
#
# 示例 1：
#
# 输入：nums = [3,10,5,25,2,8]
# 输出：28
# 解释：最大运算结果是 5 XOR 25 = 28.
# 示例 2：
#
# 输入：nums = [0]
# 输出：0
# 示例 3：
#
# 输入：nums = [2,4]
# 输出：6
# 示例 4：
#
# 输入：nums = [8,10,2]
# 输出：10
# 示例 5：
#
# 输入：nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# 输出：127
#
# 提示：
#
# 1 <= nums.length <= 2 * 104
# 0 <= nums[i] <= 231 - 1


class Trie:
    def __init__(self, val):
        self.val = val
        self.child = {}


class Solution:
    def findMaximumXOR(self, nums):
        maxXor = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                tmpXor = nums[i] ^ nums[j]
                if tmpXor > maxXor:
                    maxXor = tmpXor
        return maxXor

    def findMaximumXOR_3(self, nums):
        # 最高位的二进制位编号为 30
        HIGH_BIT = 30

        x = 0
        for k in range(HIGH_BIT, -1, -1):
            seen = set()
            # 将所有的 pre^k(a_j) 放入哈希表中
            for num in nums:
                # 如果只想保留从最高位开始到第 k 个二进制位为止的部分
                # 只需将其右移 k 位
                seen.add(num >> k)

            # 目前 x 包含从最高位开始到第 k+1 个二进制位为止的部分
            # 我们将 x 的第 k 个二进制位置为 1，即为 x = x*2+1
            x_next = x * 2 + 1
            found = False

            # 枚举 i
            for num in nums:
                if x_next ^ (num >> k) in seen:
                    found = True
                    break

            if found:
                x = x_next
            else:
                # 如果没有找到满足等式的 a_i 和 a_j，那么 x 的第 k 个二进制位只能为 0
                # 即为 x = x*2
                x = x_next - 1

        return x

    def findMaximumXOR_2(self, nums):
        # 取得最大长度
        L = len(format(max(nums), 'b')) - 1
        # 构建前缀树
        root = Trie(-1)
        for n in nums:
            curr = root
            for i in range(L, -1, -1):

                v = (n >> i) & 1
                if v not in curr.child:
                    curr.child[v] = Trie(v)

                curr = curr.child[v]
        res = 0

        # 搜索
        for n in nums:
            curr = root
            total = 0
            for i in range(L, -1, -1):
                v = (n >> i) & 1
                if 1 - v in curr.child:
                    total = total * 2 + 1
                    curr = curr.child[1 - v]
                else:
                    total = total * 2
                    curr = curr.child[v]

            # print(n, total)
            res = max(res, total)

        return res


if __name__ == '__main__':
    a = Solution()
    print(a.findMaximumXOR([3, 10, 5, 25, 2, 8]))
