def setZeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    row_flags = [0] * rows
    col_flags = [0] * cols

    # Step 1: Store row and column markers
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                row_flags[i] = 1
                col_flags[j] = 1

    # Step 2: Set matrix[i][j] = 0 if in marked row or column
    for i in range(rows):
        for j in range(cols):
            if row_flags[i] == 1 or col_flags[j] == 1:
                matrix[i][j] = 0
mat = [
    [1, 1, 1,1],
    [1, 0, 1,0],
    [1, 1, 1,1]
]

setZeroes(mat)
print(mat)