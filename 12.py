def search(a, x) -> int:
    """
    Recursively checks whether the value x exists in list a.

    Args:
        a (list): A list of integer or string values.
        x (str): The target value to search for.

    Returns:
        int: 1 if x is found in the list, otherwise 0.
    """

    if len(a) == 0:
        return 0
    if a[0] == x:
        return 1
    return search(a[1:], x)


def main() -> None:
    """
    The main function that reads input, processes data,
    and prints the result of recursive search.
    """

    a = input("Введите список через пробел: ").split()
    x = input("Введите значение для поиска: ")
    print('Если число x содержится в списке: 1. В обратном случае: 0')
    print('Результат: ', search(a, x))


if __name__ == '__main__':
    main()
