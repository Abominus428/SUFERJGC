from fractions import Fraction

def matrix_scalar_multiply(A, scalar):
    scalar_fraction = Fraction(scalar)
    result = []

    for i in range(len(A)):
        row = []
        for j in range(len(A[i])):
            product = Fraction(A[i][j]) * scalar_fraction  # 计算标量乘法
            row.append(product)
        result.append(row)

    return result