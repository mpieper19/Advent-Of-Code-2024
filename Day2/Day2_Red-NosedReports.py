from typing import List


def read_input() -> List[List[int]]:
    """
    Reads input from the user and returns a matrix of integers.

    The user is expected to input a matrix of integers with each row
    separated by a newline and each column separated by a space. The
    input is finished when the user enters a blank line.

    Returns:
        list of lists of int: The matrix of integers read from the user.
    """

    matrix = []

    while True:
        user_input = input()
        if not user_input:
            break
        matrix.append(list(map(int, user_input.split())))

    return matrix


def count_safe_occurances(matrix: List[int]) -> int:
    """
    Counts the number of safe sequences in a matrix of integers.

    A safe sequence is one which is either strictly increasing or decreasing
    by at most 3 at any point.

    Args:
        matrix (list of lists of int): The matrix of integers to be checked.

    Returns:
        int: The number of safe sequences in the matrix.
    """
    safe_occurances = 0

    for row in matrix:
        if all(row[i] < row[i+1] and abs(row[i+1] - row[i]) <= 3
               for i in range(len(row)-1)):
            safe_occurances += 1
        elif all(row[i] > row[i+1] and abs(row[i+1] - row[i]) <= 3
                 for i in range(len(row)-1)):
            safe_occurances += 1
        else:
            pass

    return safe_occurances


if __name__ == "__main__":
    matrix = read_input()
    print(count_safe_occurances(matrix))
