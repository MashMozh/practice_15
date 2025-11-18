def combin(n, k) -> int:
    """
    Recursively computes the binomial coefficient C(n, k),
    also known as the number of combinations.

    Args:
        n (int): The size of the set.
        k (int): The number of chosen elements.

    Returns:
        int: The number of k-combinations from n elements.
    """

    if k == 0 or k == n:
        return 1

    return combin(n - 1, k - 1) + combin(n - 1, k)


def main() -> None:
    """
    Reads input values n and k from the user,
    computes their binomial coefficient using recursion,
    and prints the result.
    """
    n = int(input('Введите число n: '))
    k = int(input('введите число k: '))
    print('Комбинаторное сочетание: ', combin(n, k))


if __name__ == "__main__":
    main()
