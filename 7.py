def nod(a, b) -> int:
    """
    Recursively computes the greatest common divisor (GCD)
    of two natural numbers using the Euclidean algorithm.

    Args:
        a (int): The first natural number.
        b (int): The second natural number.

    Returns:
        int: The greatest common divisor of a and b.
    """
    if a % b == 0:
        return b
    return nod(b, a % b)


def main() -> None:
    """
    The main function that reads two integers
    from the user,
    computes their GCD using a recursive function,
    and prints the result.
    """
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    print('Наибольший общий делитель: ', nod(a, b))


if __name__ == "__main__":
    main()
