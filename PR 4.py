"""
DATA ANALYZER AND TRANSFORMER

This program demonstrates:
1. Built-in functions
2. User-defined functions with __doc__
3. Recursion
4. Lambda functions
5. Returning multiple values
6. Sorting and transforming 1D and 2D arrays (lists)
"""

# ---------------------------------
# 1D ARRAY FUNCTIONS
# ---------------------------------

def analyze_1d(data):
    """
    Analyze a 1D list and return total, average,
    maximum and minimum values.
    """
    if not data:
        return 0, 0, None, None

    total = sum(data)
    average = total / len(data)
    maximum = max(data)
    minimum = min(data)

    return total, average, maximum, minimum


def sort_ascending(data):
    """
    Sort list in ascending order.
    """
    return sorted(data)


def sort_descending(data):
    """
    Sort list in descending order.
    """
    return sorted(data, reverse=True)


def square_transform(data):
    """
    Square each element using lambda function.
    """
    return list(map(lambda x: x ** 2, data))


def filter_even(data):
    """
    Return only even numbers using lambda.
    """
    return list(filter(lambda x: x % 2 == 0, data))


# ---------------------------------
# RECURSION FUNCTION
# ---------------------------------

def recursive_sum(data):
    """
    Find sum of list using recursion.
    """
    if len(data) == 0:
        return 0

    return data[0] + recursive_sum(data[1:])


# ---------------------------------
# 2D ARRAY FUNCTIONS
# ---------------------------------

def analyze_2d(matrix):
    """
    Analyze 2D array.
    Returns rows, columns and total.
    """
    if not matrix:
        return 0, 0, 0

    rows = len(matrix)
    cols = len(matrix[0])
    total = sum(sum(row) for row in matrix)

    return rows, cols, total


def row_totals(matrix):
    """
    Return sum of each row.
    """
    return list(map(sum, matrix))


def sort_2d_by_column(matrix, column):
    """
    Sort matrix based on any column.
    """
    if not matrix:
        return matrix

    if column < 0 or column >= len(matrix[0]):
        print("Invalid Column Number!")
        return matrix

    return sorted(matrix, key=lambda row: row[column])


def multiply_2d(matrix, factor):
    """
    Multiply each element by given factor.
    """
    return [[item * factor for item in row] for row in matrix]


# ---------------------------------
# DISPLAY FUNCTIONS
# ---------------------------------

def display_1d_analysis():
    """
    Display all 1D array operations.
    """
    print("\n" + "=" * 50)
    print("1D ARRAY ANALYSIS")
    print("=" * 50)

    data = [10, 20, 30, 40, 50, 60]

    print("Original Data :", data)

    total, avg, maximum, minimum = analyze_1d(data)

    print("Total         :", total)
    print("Average       :", avg)
    print("Maximum       :", maximum)
    print("Minimum       :", minimum)

    print("\nAscending Sort :", sort_ascending(data))
    print("Descending Sort:", sort_descending(data))
    print("Squared Values :", square_transform(data))
    print("Even Numbers   :", filter_even(data))
    print("Recursive Sum  :", recursive_sum(data))


def display_2d_analysis():
    """
    Display all 2D array operations.
    """
    print("\n" + "=" * 50)
    print("2D ARRAY ANALYSIS")
    print("=" * 50)

    matrix = [
        [5, 2, 9],
        [1, 7, 3],
        [8, 4, 6]
    ]

    print("Original Matrix:")
    for row in matrix:
        print(row)

    rows, cols, total = analyze_2d(matrix)

    print("\nRows    :", rows)
    print("Columns :", cols)
    print("Total   :", total)

    print("\nRow Totals:")
    print(row_totals(matrix))

    print("\nSorted by Column 1:")
    sorted_matrix = sort_2d_by_column(matrix, 1)

    for row in sorted_matrix:
        print(row)

    print("\nMultiplied Matrix (Factor = 2):")

    multiplied_matrix = multiply_2d(matrix, 2)

    for row in multiplied_matrix:
        print(row)


# ---------------------------------
# MAIN FUNCTION
# ---------------------------------

def main():
    """
    Main driver function.
    """

    print("=" * 60)
    print("      DATA ANALYZER AND TRANSFORMER")
    print("=" * 60)

    display_1d_analysis()
    display_2d_analysis()

    print("\n" + "=" * 60)
    print("FUNCTION DOCUMENTATION")
    print("=" * 60)

    print("\nDocstring of analyze_1d():")
    print(analyze_1d.__doc__)

    print("\nProgram Executed Successfully!")


# ---------------------------------
# PROGRAM EXECUTION
# ---------------------------------

if __name__ == "__main__":
    main()
