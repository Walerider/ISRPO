def check_even_rows_ascending(matrix):
    even_sums = []

    for i in range(0, len(matrix), 2):
        row_sum = sum(matrix[i])
        even_sums.append(row_sum)

    for i in range(1, len(even_sums)):
        if even_sums[i] <= even_sums[i-1]:
            return False

    return True

def check_matrices(zzz):
    for idx, matrix in enumerate(zzz, 1):
        if check_even_rows_ascending(matrix):
            print(f"Массив {idx}: Суммы элементов четных строк образуют возрастающую последовательность.")
        else:
            print(f"Массив {idx}: Суммы элементов четных строк НЕ образуют возрастающую последовательность.")

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [10, 20, 30],
    [40, 50, 60],
    [5, 6, 7],
    [1, 2, 3]
]

check_matrices([matrix1, matrix2])

# zxc