from fractions import Fraction

def matrix_multiply(A, B):
    # 检查矩阵 A 的列数是否与矩阵 B 的行数相等
    if len(A[0]) != len(B):
        raise ValueError("矩阵 A 的列数与矩阵 B 的行数不匹配，无法进行乘法。")

    result = []
    
    for i in range(len(A)):
        result.append([])
        for j in range(len(B[0])):
            sum_value = Fraction(0)
            for k in range(len(A[0])):
                # 使用 Fraction 进行乘法并累加
                product = Fraction(A[i][k]) * Fraction(B[k][j])
                sum_value += product
            result[i].append(sum_value)
    
    return result
