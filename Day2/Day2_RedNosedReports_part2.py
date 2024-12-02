from typing import List
from Day2_RedNosedReports_part1 import read_input


def count_safe_occurances(matrix: List[int]) -> int:
    """
    Counts the number of safe sequences in a matrix of integers.

    A safe sequence is one that is either strictly increasing or decreasing by at 
    most 3 at any point, or can become such a sequence by removing at most one element.

    Args:
        matrix (List[List[int]]): The matrix of integers to be checked.

    Returns:
        int: The number of safe sequences in the matrix.
    """
    def is_safe(row: List[int]) -> bool:
        """
        Checks if a row is a safe sequence.

        A safe sequence is one that is either strictly increasing or decreasing by at 
        most 3 at any point, or can become such a sequence by removing at most one element.

        Args:
            row (List[int]): The row to be checked.

        Returns:
            bool: Whether the row is a safe sequence.
        """
        if (all(row[i] < row[i+1] and abs(row[i+1] - row[i]) <= 3 for i in range(len(row)-1)) or
            all(row[i] > row[i+1] and abs(row[i+1] - row[i]) <= 3 for i in range(len(row)-1))):
            return True
        
        for i in range(len(row)):
            popped_row = row.copy()
            popped_row.pop(i)
            if (all(popped_row[i] < popped_row[i+1] and abs(popped_row[i+1] - popped_row[i]) <= 3 for i in range(len(popped_row)-1)) or
                all(popped_row[i] > popped_row[i+1] and abs(popped_row[i+1] - popped_row[i]) <= 3 for i in range(len(popped_row)-1))):
                return True

        return False

    safe_occurances = 0

    for row in matrix:
        if is_safe(row):
            safe_occurances += 1
        continue

    return safe_occurances


if __name__ == "__main__":
    matrix = read_input()
    print(count_safe_occurances(matrix))
