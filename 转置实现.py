def matrix_transpose(A):
    result = []
    for i in range(len(A[0])):
        row = []
        for j in range(len(A)):
            row.append(A[j][i])
        result.append(row)
    
    return result

