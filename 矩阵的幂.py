from fractions import Fraction

def matrix_power(A, n):
    result = [[Fraction(value) for value in row] for row in A]  # 复制矩阵A

    for _ in range(1, n):
        result = matrix_multiply(result, A)  # 重复调用矩阵乘法

    return result