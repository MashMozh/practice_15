def sum_progress(a1, r, n) -> int:
    """
    Recursively computes the sum of the first n terms
    of an arithmetic progression.

    Args:
        a1 (int): The first term of the progression.
        r (int): The common difference between terms.
        n (int): The number of terms to sum.

    Returns:
        int: The sum of the first n terms of the progression.
    """
    if n == 1:
        return a1
    return sum_progress(a1, r, n - 1) + (a1 + r * (n - 1))


def main() -> None:
    """
    The main function that receives input from the user,
    computes the progression sum and prints the result.
    """
    a1 = int(input('Введите первый член прогрессии: '))
    r = int(input('Введите разность прогрессии: '))
    n = int(input('Введите номер элемента прогрессии: '))
    print(sum_progress(a1, r, n))


if __name__ == '__main__':
    main()
