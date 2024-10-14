from fractions import Fraction

def matrix_subtract(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[i])):
            # 使用 Fraction 进行减法
            diff = Fraction(A[i][j]) - Fraction(B[i][j])
            row.append(diff)
        result.append(row)
    
    return result
