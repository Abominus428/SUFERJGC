from fractions import Fraction

def matrix_determinant(A):
    n = len(A)

    if n == 1:
        return A[0][0]

    if n == 2:
        det2x2 = Fraction(A[0][0]) * Fraction(A[1][1]) - Fraction(A[0][1]) * Fraction(A[1][0])
        return det2x2

    determinant = Fraction(0)
    
    for col in range(n):
        minor = [row[:col] + row[col+1:] for row in A[1:]]  # 获取子矩阵
        cofactor_result = matrix_determinant(minor)  # 递归计算子矩阵的行列式
        cofactor = Fraction(A[0][col]) * cofactor_result
        determinant += cofactor if col % 2 == 0 else -cofactor

    return determinant