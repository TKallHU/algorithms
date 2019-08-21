"""
author: buppter
datetime: 2019/8/21 19:17

题目描述
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.


解决思路：
每次打印第一行，然后矩阵逆时针旋转90度，重复之前步骤
"""


class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if not matrix:
            return []
        res = []
        while matrix:
            res += matrix.pop(0)
            if matrix:
                matrix = self.turn(matrix)
        return res

    def turn(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        res = []

        for i in range(cols - 1, -1, -1):
            new_res = []
            for j in range(rows):
                new_res.append(matrix[j][i])

            res.append(new_res)
        return res

