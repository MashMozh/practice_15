def maxlist(a) -> int:
    """
    Recursively finds the maximum element in a list of integers.

    Args:
        a (list): A list of integers.

    Returns:
        int: The maximum value in the list.
    """
    
    if len(a) == 1:
        return a[0]
    return a[0] if a[0] > maxlist(a[1:]) else maxlist(a[1:])


def main() -> None:
    """
    Main function: reads a list of integers from input,
    calls maxlist() and prints the result.
    """
    
    a = input('Введите целые числа через пробел: ').split()
    print(maxlist(a))


if __name__ == "__main__":
    main()
  
