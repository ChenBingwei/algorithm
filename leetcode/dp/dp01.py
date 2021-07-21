# 62. 不同路径
# 一个机器人位于一个 m x n网格的左上角 （起始点在下图中标记为 “Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
# 问总共有多少条不同的路径？

# 示例 2：
# 输入：m = 3, n = 2
# 输出：3
# 解释：
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向下

# 示例 3：
# 输入：m = 7, n = 3
# 输出：28

# 示例 4：
# 输入：m = 3, n = 3
# 输出：6

class Solution:
    @staticmethod
    def my_solution(m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 0

        for i in range(0, m):
            for j in range(0, n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        # for line in dp:
        #     print(line)
        return dp[m - 1][n - 1]

    @staticmethod
    def unique_paths(m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                elif i > 0:
                    dp[i][j] = dp[i - 1][j]
                elif j > 0:
                    dp[i][j] = dp[i][j - 1]

        return dp[m - 1][n - 1]

    @staticmethod
    def unique_paths_plus(m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        for line in dp:
            print(line)
        return dp[m][n]


if __name__ == '__main__':
    res = Solution.my_solution(3, 7)
    print(res)
    res2 = Solution.unique_paths(3, 7)
    print(res2)
    res3 = Solution.unique_paths_plus(3, 7)
    print(res3)
