def setZeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Use a placeholder value
    PLACEHOLDER = -99999

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                # Mark row
                for k in range(cols):
                    if matrix[i][k] != 0:
                        matrix[i][k] = PLACEHOLDER
                # Mark column
                for k in range(rows):
                    if matrix[k][j] != 0:
                        matrix[k][j] = PLACEHOLDER

    # Convert all placeholders to 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == PLACEHOLDER:
                matrix[i][j] = 0

mat = [
    [1, 1, 1,1],
    [1, 0, 1,0],
    [1, 1, 1,1]
]

setZeroes(mat)
print(mat)
# Output: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]