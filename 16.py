def ten_to_n(x, n) -> str:
    """
    Converts a natural number x from decimal system
    to base-n system (2 ≤ n ≤ 16) using a recursive algorithm.

    Args:
        x (int): A natural number in decimal representation.
        n (int): The target numeral system base (from 2 to 16).

    Returns:
        str: The representation of number x in base-n as a string.
    """

    elements = "0123456789ABCDEF"

    if x < n:
        return elements[x]

    return ten_to_n(x // n, n) + elements[x % n]


def main() -> None:
    """
    The main function that reads user input,
    converts number x to base-n representation using recursion
    and prints the result.
    """

    x = int(input('Введите натуральное число: '))
    n = int(input('Введите желаемую систему счисления(в виде числа): '))
    print(ten_to_n(x, n))


if __name__ == "__main__":
    main()
