from fractions import Fraction

def matrix_rank(A):
    rows = len(A)
    cols = len(A[0])
    mat = [[Fraction(value) for value in row] for row in A]  # 确保矩阵中的元素为 Fraction 对象
    rank = 0

    # 逐行处理
    for row in range(rows):
        pivot_found = False

        # 检查当前行的主元素
        if mat[row][row] != 0:
            pivot_found = True
        else:
            # 尝试与下面的行交换，找到非零主元素
            for i in range(row + 1, rows):
                if mat[i][row] != 0:
                    mat[row], mat[i] = mat[i], mat[row]  # 行交换
                    pivot_found = True
                    break

        # 如果找到了有效的主元素
        if pivot_found:
            rank += 1  # 每找到一个非零主元素，秩加一

            # 将主元素下方的所有元素消为 0
            for i in range(row + 1, rows):
                if mat[i][row] != 0:
                    ratio = mat[i][row] / mat[row][row]  # 计算比率
                    for j in range(row, cols):
                        mat[i][j] -= ratio * mat[row][j]  # 行减法
        # 如果主元素为 0 且没有行交换成功，则跳过该行

    return rank

