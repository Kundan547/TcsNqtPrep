def setZeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    col0 = 1  # To handle first column separately

    # Step 1: Use matrix as markers
    for i in range(rows):
        if matrix[i][0] == 0:
            col0 = 0
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0


    # Step 2: Apply markers in reverse
    for i in reversed(range(rows)):
        for j in reversed(range(1, cols)):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
        if col0 == 0:
            matrix[i][0] = 0
mat = [
    [1, 1, 1,1],
    [1, 0, 1,0],
    [1, 1, 1,1]
]
setZeroes(mat)
print(mat)