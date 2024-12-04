from Day3_MullItOver_part1 import read_input
import re


def mul_nums(inp: str) -> int:

    """
    Multiplies pairs of numbers found in a specific format within a string.

    This function searches the input string for occurrences of the format 
    'mul(int1,int2)', extracts the integers, multiplies each pair, and returns 
    the total sum of all these multiplications, but only if the previous 
    occurrence was 'do()'. If the previous occurrence was 'don't()', the next 
    multiplication is ignored.

    Args:
        inp (str): The input string to search for number pairs.

    Returns:
        int: The total sum of the multiplied pairs.
    """

    regex_pattern = r"(do\(\))|(don't\(\))|mul\(([0-9]+,[0-9]+)\)"
    result = re.findall(regex_pattern, inp)

    is_enabled = True
    total = 0

    for i in result:
        do, dont, mul = i
        if do:
            is_enabled = True
        elif dont:
            is_enabled = False
        else:
            if is_enabled:
                int1, int2 = mul.split(",")
                total += (int(int1) * int(int2))

    return total


if __name__ == "__main__":
    inp = read_input("Day3/input.txt")
    print(mul_nums(inp))
