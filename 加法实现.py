//加法
from fractions import Fraction

def matrix_add(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[i])):
            # 使用 Fraction 进行加法
            sum_value = Fraction(A[i][j]) + Fraction(B[i][j])
            row.append(sum_value)
        result.append(row)
    
    return result
