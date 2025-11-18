def pownum(a, n) -> int:
    """
    Computes the power of a number using a recursive algorithm.

    Args:
        a (int): The base number.
        n (int): The degree of variable a.

    Returns:
        int: The result of a raised to the power n.
    """
    if n == 0:
        return 1
    return a * pownum(a, n - 1)


def main() -> None:
    """
    The main function that reads input values,
    computes the power using pownum(),
    and prints the resul.
    """

    a = int(input("Введите число a: "))
    n = int(input("Введите показатель степени n: "))
    print(pownum(a, n))


if __name__ == "__main__":
    main()
