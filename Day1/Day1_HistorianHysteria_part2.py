from typing import List
from Day1_HistorianHysteria_part1 import read_input


def find_similarity_score(left_list: List[int], right_list: List[int]) -> int:
    """
    Calculates the similarity score between two lists of integers.

    The similarity score is calculated by finding the common elements between
    the two lists, and for each common element, multiplying the element by its
    frequency in the second list. The sum of these scores is then returned.

    Args:
        left_list (List[int]): The first list of integers.
        right_list (List[int]): The second list of integers.

    Returns:
        int: The similarity score between the two lists.
    """
    similarity_score = []
    for i in left_list:
        if i in right_list:
            score = i * (right_list.count(i))
            similarity_score.append(score)

    return sum(similarity_score)


if __name__ == "__main__":
    left_list, right_list = read_input()
    print(find_similarity_score(left_list, right_list))
