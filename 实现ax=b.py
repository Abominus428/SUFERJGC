def solve_axb(A, B):
    if len(A) != len(A[0]) or len(A) != len(B):
        raise ValueError("AX = B 无法求解，因为矩阵 A 不是方阵或 B 的维度与 A 不匹配。")

    # 计算 A 的逆矩阵
    inverse_A = matrix_inverse(A)

    if inverse_A is None:
        raise ValueError("A 矩阵不可逆，无法求解 AX = B")

    # X = A^-1 * B
    result = matrix_multiply(inverse_A, B)
    
    return result