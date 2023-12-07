def triangle(numRows):
    if numRows == 0:
        return []
    triangle = [[1]]
    for i in range(1, numRows):
        prev = triangle[-1]
        current_row = [1]
        for j in range(1, i):
            current_row.append(prev[j - 1] + prev[j])
        current_row.append(1)
        triangle.append(current_row)
    return triangle
numRows = int(input("numRows = "))
output = triangle(numRows)
print(output)
