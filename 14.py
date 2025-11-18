def numbers(x) -> None:
    """
    Recursively prints the digits of a natural number x
    in reverse order, one digit per line.

    Args:
        x (int): A natural number whose digits will be printed.

    Returns:
        None: The function only prints digits.
    """

    print(x % 10)
    if x >= 10:
        numbers(x // 10)


def main() -> None:
    """
    Main function that reads user input
    and prints the digits of the number in reverse order.

    Returns:
        None
    """

    x = int(input('Введите натуральное число: '))
    numbers(x)


if __name__ == '__main__':
    main()
