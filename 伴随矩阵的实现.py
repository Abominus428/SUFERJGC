from fractions import Fraction

def matrix_adjugate(A):
    n = len(A)
    adjugate = [[Fraction(0) for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            # 构造子矩阵，删除第 i 行和第 j 列
            sub_matrix = [row[:j] + row[j+1:] for row in (A[:i] + A[i+1:])]

            # 计算余子式的行列式
            cofactor_det = matrix_determinant(sub_matrix)

            # 代数余子式
            adjugate[j][i] = Fraction((-1) ** (i + j)) * Fraction(cofactor_det)

    return adjugate