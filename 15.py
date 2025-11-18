def ten_to_bin(x) -> str:
    """
    Converts a natural number from decimal representation
    into its binary representation using a recursive algorithm.

    Args:
        x (int): A natural number to convert.

    Returns:
        str: The binary representation of the number as a string.
    """


    def helper(n) -> str:
        """
        Recursively converts the given number into binary form.

        Args:
            n (int): A natural number or intermediate value.

        Returns:
            str: Partial binary string.
        """

        if n < 2:
            return str(n)
        return helper(n // 2) + str(n % 2)

    return helper(x)


def main() -> None:
    """
    The main function that reads user input,
    performs the conversion and prints the result.
    """

    x = int(input("Введите натуральное число: "))
    print('Число x в двоичной системе: ', ten_to_bin(x))


if __name__ == "__main__":
    main()
