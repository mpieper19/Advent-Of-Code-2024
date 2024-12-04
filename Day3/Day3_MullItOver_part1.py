import re


def read_input(file_path: str) -> str:
    """
    Reads a file and returns its contents as a string.

    Args:
        file_path (str): The path to the file to read.

    Returns:
        str: The contents of the file.
    """
    with open(file_path, "r") as f:
        return f.read()


def mul_nums(inp: str) -> int:
    """
    Multiplies pairs of numbers found in a specific format within a string.

    This function searches the input string for occurrences of the format 
    'mul(int1,int2)', extracts the integers, multiplies each pair, and returns 
    the total sum of all these multiplications.

    Args:
        inp (str): The input string to search for number pairs.

    Returns:
        int: The total sum of the multiplied pairs.
    """

    regex_pattern = r"mul\(([0-9]+,[0-9]+)\)"
    result = re.findall(regex_pattern, inp)

    total = 0

    for i in result:
        int1, int2 = i.split(",")
        total += (int(int1) * int(int2))

    return total


if __name__ == "__main__":
    inp = read_input("Day3/input.txt")
    print(mul_nums(inp))
