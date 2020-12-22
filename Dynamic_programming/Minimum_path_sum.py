#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个包含非负整数的 m x n网格grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例 1：


输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
示例 2：

输入：grid = [[1,2,3],[4,5,6]]
输出：12

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100
"""
from common import utils


@utils.print_time
def func_1(grid_list):
    def minPathSum(grid):
        m = len(grid)
        n = len(grid[0])
        return dp(grid, m - 1, n - 1)

    def dp(grid, i, j):
        # base case
        if i == j == 0:
            return grid[0][0]

        # 如果索引出界，返回一大很大的值，
        # 保证在取最小值的时候不会被取到
        if i < 0 or j < 0:
            return float("inf")

        return grid[i][j] + min(
            dp(grid, i - 1, j),
            dp(grid, i, j - 1)
        )

    return minPathSum(grid_list)


@utils.print_time
def func_2(grid_list):
    memo = {}

    def minPathSum(grid):
        m = len(grid)
        n = len(grid[0])

        return dp(grid, m - 1, n - 1)

    def dp(grid, i, j):
        nonlocal memo
        tag = "{}X{}".format(i, j)
        if i == j == 0:
            return grid[0][0]
        # 如果索引出界，返回一大很大的值，
        # 保证在取最小值的时候不会被取到
        if i < 0 or j < 0:
            return float("inf")
        if tag in memo:
            return memo[tag]

        memo[tag] = grid[i][j] + min(
            dp(grid, i - 1, j),
            dp(grid, i, j - 1)
        )
        return memo[tag]

    return minPathSum(grid_list)


@utils.print_time
def func_3(grid_list):
    def minPathSum(grid):
        m = len(grid)
        n = len(grid[0])
        dp = {'0X0': grid[0][0]}
        for i in range(1, m):
            dp['{}X0'.format(i)] = dp['{}X0'.format(i - 1)] + grid[i][0]
        for j in range(1, n):
            dp['0X{}'.format(j)] = dp['0X{}'.format(j - 1)] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp['{}X{}'.format(i, j)] = grid[i][j] + min(
                    dp['{}X{}'.format(i - 1, j)],
                    dp['{}X{}'.format(i, j - 1)]
                )
        return dp['{}X{}'.format(m - 1, n - 1)]

    return minPathSum(grid_list)


if __name__ == '__main__':
    grid = [
        [5, 1, 0, 4, 0, 1, 1, 6, 7, 3, 9, 9, 4, 6, 8, 1],
        [9, 1, 0, 6, 4, 2, 8, 0, 1, 6, 0, 2, 7, 9, 0, 4],
        [3, 2, 0, 3, 3, 3, 1, 3, 7, 3, 2, 1, 1, 2, 2, 0],
        [5, 2, 8, 2, 7, 6, 2, 0, 5, 3, 2, 4, 4, 4, 8, 9],
        [7, 0, 5, 2, 4, 6, 7, 1, 1, 1, 2, 2, 6, 6, 4, 1],
        [0, 3, 5, 9, 1, 8, 0, 6, 3, 4, 0, 9, 9, 0, 9, 8],
        [3, 4, 0, 7, 2, 8, 0, 4, 9, 4, 8, 5, 2, 5, 9, 4],
        [0, 4, 4, 1, 4, 6, 0, 7, 0, 2, 7, 1, 3, 8, 9, 8],
        [2, 0, 7, 4, 0, 7, 0, 1, 1, 1, 9, 5, 6, 8, 9, 6],
        [4, 3, 9, 9, 1, 9, 8, 4, 2, 7, 5, 7, 5, 5, 5, 9],
        [7, 4, 6, 9, 1, 8, 0, 4, 9, 9, 9, 7, 9, 8, 3, 4],
        [4, 3, 5, 7, 4, 5, 1, 8, 3, 7, 7, 0, 4, 4, 2, 3],
        [8, 0, 2, 9, 8, 2, 5, 8, 4, 4, 7, 3, 5, 1, 9, 1],
        [6, 4, 8, 2, 2, 2, 1, 7, 1, 8, 7, 5, 5, 1, 0, 3],
        [1, 2, 5, 0, 6, 0, 0, 0, 7, 7, 6, 4, 0, 5, 5, 8],
        [2, 5, 1, 4, 9, 4, 1, 0, 2, 0, 5, 7, 4, 7, 3, 5],
        [9, 8, 7, 8, 8, 9, 8, 5, 9, 6, 9, 9, 2, 6, 0, 6],
        [4, 1, 2, 3, 5, 5, 4, 9, 5, 1, 9, 9, 9, 2, 7, 0],
        [0, 6, 8, 0, 6, 9, 8, 7, 5, 7, 8, 9, 6, 8, 5, 0]
    ]
    # func_1(grid)
    func_2(grid)
    func_3(grid)
