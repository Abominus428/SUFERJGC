def matrix_lu(A):
    n = len(A)
    L = [[0] * n for _ in range(n)]
    U = [row[:] for row in A]  # 创建 A 的副本

    for i in range(n):
        L[i][i] = 1  # L 矩阵的对角线元素设为 1
        for j in range(i + 1, n):
            factor = U[j][i] / U[i][i]  # 计算消元系数
            for k in range(n):
                U[j][k] -= factor * U[i][k]  # 对 U 矩阵进行消元操作
            L[j][i] = factor  # 将消元系数存入 L 矩阵

    return L, U


