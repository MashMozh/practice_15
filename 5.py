def mod_number(a, b) -> int:
    """
    Recursively computes the remainder of dividing 'a' by 'b'
    using repeated subtraction.

    Args:
        a (int): The dividend, natural number.
        b (int): The divisor, natural number.

    Returns:
        int: The remainder of a divided by b.
    """
    if a < b:
        return a
    return mod_number(a - b, b)


def main() -> None:
    """
    The main function that coordinates the program execution:
    reads input from the user, calls the recursive mod_number
    function, and prints the result.
    """
    a = int(input("Введите делимое: "))
    b = int(input("Введите делитель: "))
    print(mod_number(a, b))


if __name__ == "__main__":
    main()
