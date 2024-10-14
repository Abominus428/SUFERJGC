from fractions import Fraction

def matrix_inverse(A):
    # 计算行列式
    determinant = matrix_determinant(A)
    
    if determinant == 0:
        raise ValueError("由于行列式为 0，矩阵 A 不可逆。")

    # 计算伴随矩阵
    adjugate_matrix = matrix_adjugate(A)
    
    n = len(A)
    inverse = [[Fraction(0) for _ in range(n)] for _ in range(n)]

    # 通过 A^-1 = adj(A) / det(A) 计算逆矩阵
    for i in range(n):
        for j in range(n):
            numerator = Fraction(adjugate_matrix[i][j])
            denominator = Fraction(determinant)
            inverse[i][j] = numerator / denominator

    return inverse
