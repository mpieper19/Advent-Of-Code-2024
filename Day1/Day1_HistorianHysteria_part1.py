from typing import List


def read_input() -> tuple[List[int], List[int]]:
    """
    Reads input from the user and returns two sorted lists of integers.

    Returns:
        tuple of two lists: The two sorted lists of integers read from the
        user.
    """
    left_list = []
    right_list = []
    while True:
        user_input = input()
        if not user_input:
            break
        int1, int2 = map(int, user_input.split())
        left_list.append(int1)
        right_list.append(int2)

    return left_list, right_list


def get_differences(left: List[int], right: List[int]) -> int:
    """
    Calculates the sum of the absolute differences between corresponding
    elements of two sorted lists.

    Args:
        left (List[int]): The first sorted list of integers.
        right (List[int]): The second sorted list of integers.

    Returns:
        int: The sum of the absolute differences between corresponding
        elements in the two lists.
    """
    distances = []
    sorted_left = sorted(left)
    sorted_right = sorted(right)
    for i in range(len(sorted_left)):
        distances.append(abs(sorted_left[i] - sorted_right[i]))

    return sum(distances)


if __name__ == "__main__":
    left_list, right_list = read_input()
    print(get_differences(left_list, right_list))
