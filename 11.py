def ind_maxlist(a) -> int:
    """
    Recursively finds the index of the maximum element in the list.

    Args:
        a (list): List of integers.

    Returns:
        int: Index of the maximum element.
    """

    if len(a) == 1:
        return 0
    if a[ind_maxlist(a[:-1])] >= a[-1]:
        return ind_maxlist(a[:-1])
    else:
        return len(a) -1


def main() -> None:
    """
    Reads a list of integers from input and prints the index
    of the maximum element using recursion.
    """

    a = input('Введите целые числа через пробел: ').split()
    print('Индекс максимального элемента: ', ind_maxlist(a))


if __name__ == "__main__":
    main()
