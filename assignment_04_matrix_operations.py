
def read_matrix(rows, cols, label=""):
    """Read a matrix of size rows x cols from the user, one row per line."""
    matrix = []
    for i in range(rows):
        while True:
            row_input = input(f"Enter row {i + 1}{label}: ").split()
            row = [int(val) for val in row_input]
            if len(row) != cols:
                print(f"Error: expected {cols} values, got {len(row)}. Try again.")
                continue
            matrix.append(row)
            break
    return matrix


def print_matrix(matrix):
    """Display a matrix in a neat, aligned grid format."""
    if not matrix:
        print("(empty matrix)")
        return
    # Find the widest number so every column lines up
    width = max(len(str(val)) for row in matrix for val in row)
    for row in matrix:
        print("  ".join(str(val).rjust(width) for val in row))


def transpose(matrix):
    """Return the transpose of a matrix using nested loops."""
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result


def add_matrices(a, b):
    """Return the element-wise sum of two same-sized matrices."""
    rows = len(a)
    cols = len(a[0])
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = a[i][j] + b[i][j]
    return result


def multiply_matrices(a, b):
    """Return the matrix product A x B using nested loops."""
    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])
    result = [[0] * cols_b for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += a[i][k] * b[k][j]
            result[i][j] = total
    return result


if __name__ == "__main__":

    print("=== Part A: Transpose a Matrix ===")
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))
    matrix_a = read_matrix(m, n)

    print("\nOriginal Matrix:")
    print_matrix(matrix_a)
    print("\nTransposed Matrix:")
    print_matrix(transpose(matrix_a))

    print("\n=== Part B: Add Two Matrices ===")
    rows_b = int(input("Enter number of rows for both matrices: "))
    cols_b = int(input("Enter number of columns for both matrices: "))

    print("Matrix 1:")
    matrix_1 = read_matrix(rows_b, cols_b)
    print("Matrix 2:")
    matrix_2 = read_matrix(rows_b, cols_b)

    print("\nSum of Matrices:")
    print_matrix(add_matrices(matrix_1, matrix_2))

    print("\n=== Part C: Multiply Two Matrices ===")
    rows_c1 = int(input("Enter rows for Matrix A: "))
    cols_c1 = int(input("Enter columns for Matrix A (= rows for Matrix B): "))
    cols_c2 = int(input("Enter columns for Matrix B: "))

    print("Matrix A:")
    matrix_c1 = read_matrix(rows_c1, cols_c1)
    print("Matrix B:")
    matrix_c2 = read_matrix(cols_c1, cols_c2)

    print("\nProduct of Matrices (A x B):")
    print_matrix(multiply_matrices(matrix_c1, matrix_c2))
