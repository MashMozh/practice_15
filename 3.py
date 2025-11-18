def progress(a1, r, n) -> int:
    """
    Computes the n-th term of an arithmetic
    progression using recursion.

    The progression is defined by:
        a₁ — first term
        r  — common difference
        n  — term index

    Args:
        a1 (int): The first term of the arithmetic progression.
        r (int): The common difference of the progression.
        n (int): The index of the term to compute.

    Returns:
        int: The value of the n-th term of the arithmetic 
        progression.
    """

    if n == 1:
        return a1
    return progress(a1, r, n - 1) + r


def main() -> None:
    """
    The main function that receives input from the user,
    computes the n-th term of the arithmetic progression,
    and prints the result.
    """

    a1 = int(input("Введите первый член прогрессии: "))
    r = int(input("Введите разность прогрессии: "))
    n = int(input("Введите номер члена прогрессии: "))

    print(progress(a1, r, n))


if __name__ == '__main__':
    main()
