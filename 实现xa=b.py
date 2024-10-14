def solve_xab(A, B):
    if len(A) != len(A[0]) or len(A[0]) != len(B[0]):
        raise ValueError("XA = B 无法求解，因为矩阵 A 不是方阵或 B 的维度与 A 不匹配。")

    # 计算 A 的逆矩阵
    inverse_A = matrix_inverse(A)

    if inverse_A is None:
        raise ValueError("A 矩阵不可逆，无法求解 XA = B")

    # X = B * A^-1
    result = matrix_multiply(B, inverse_A)

    return result

