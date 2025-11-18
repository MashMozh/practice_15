def function1(x) -> int:
    """
    Determines whether a given natural number x is prime using recursion.
    Returns 1 if x is prime, otherwise returns 0.

    Args:
        x (int): A natural number to check for primality.

    Returns:
        int: 1 if x is prime, 0 otherwise.
    """

    if x < 2:
        return 0

    if x == 2:
        return 1

    if x % 2 == 0:
        return 0

    def check_divisor(n: int, d: int) -> int:
        """
        Recursively checks divisors from d down to 1.

        Args:
            n (int): Number being checked.
            d (int): Current divisor.

        Returns:
            int: 1 if prime, 0 if composite.
        """

        if d == 1:
            return 1
        if n % d == 0:
            return 0
        return check_divisor(n, d - 1)

    return check_divisor(x, x - 1)


def main() -> None:
    """
    Main function that reads input and prints the primality result.
    """

    x = int(input('Введите натуральное число: '))
    print('1 - число простое, иначе - 0. Результат: ', function1(x))


if __name__ == "__main__":
    main()
