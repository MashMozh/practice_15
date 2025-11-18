def degree5(n: int) -> int:
    """
    Recursively determines the exponent of 5 for which 
    the given number n equals 5^k.

    If n is not a power of 5, the function returns -1.

    Args:
        n (int): A natural number to check.

    Returns:
        int: The exponent k such that n = 5^k, or -1 if n is not a power of 5.
    """
    if n == 1:
        return 0
    if n == 0 or n % 5 != 0:
        return -1
    return 1 + degree5(n // 5)


def main() -> None:
    """
    The main function that reads input values and prints
    the result of the degree5 function.
    """
    n = int(input('Введите число: '))
    print('Это число является пятеркой в степени: 'degree5(n))


if __name__ == "__main__":
    main()
