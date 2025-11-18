def even_list(a, n) -> list:
    """
    Recursively extracts and returns a list of even integers
    from the given list `a` containing `n` integer elements.

    The function processes the list from the end toward the beginning,
    collecting even values into a new list.

    Args:
        a (list): A list of integers.
        n (int): The number of elements in the list.

    Returns:
        list: A new list containing only even integers from `a`,
              in the same order as they appeared originally.
    """

    if n == 0:
        return []
    if a[n - 1] % 2 == 0:
        return even_list(a, n - 1) + [a[n - 1]]
    else:
        return even_list(a, n - 1)


def main() -> None:
    """
    Reads a list of integers from the user,
    calls even_list() to extract even numbers,
    and prints the resulting list.
    """

    a = input('Введите целые числа через пробел: ').split()
    print('Список четных значений: ', even_list(a, len(a)))


if __name__ == '__main__':
    main()
