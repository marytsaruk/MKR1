matrix = [
    [42, 13, 7],
    [17, 4, 82],
    [42, 36, 9]
]

num_rows = len(matrix)
num_columns = len(matrix[0])
column_sums = [0] * num_columns
for row in matrix:
    for i in range(num_columns):
        column_sums[i] += row[i]
print("Суми стовпців:", column_sums)

column_order = sorted(range(len(column_sums)), key=lambda d: column_sums[d])

sorted_matrix = [[0] * num_columns for _ in range(num_rows)]
for k in range(num_columns):
    col_index = column_order[k]
    for j in range(num_rows):
        sorted_matrix[j][k] = matrix[j][col_index]

for row in sorted_matrix:
    print(row)