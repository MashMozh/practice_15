def count(n: int) -> int:
    """
    Recursively counts the number of digits in a natural number n.

    Args:
        n (int): A natural number.

    Returns:
        int: Number of digits in n.
    """
    if n < 10:
        return 1
    return 1 + count(n // 10)


def main() -> None:
    """
    Main function that reads a natural number from
    the user and prints the number of its digits.
    """
    n = int(input('Введите натуральное число: '))
    if n <= 0:
        print("Пожалуйста, введите натуральное число(больше 0).")
    else:
        print('Количество цифр в числе: ', count(n))


if __name__ == "__main__":
    main()
