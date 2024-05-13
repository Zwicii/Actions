def divide(a: int, b: int) -> float:
    """Return the result of a division operation between two numbers.

    Args:
        a (int): The numerator.
        b (int): The denominator.

    Returns:
        float: The result of the division operation.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("You can't divide by zero!")
    return a / b


def multiply(a: int, b: int) -> int:
    """Return the result of a multiplication operation between two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The result of the multiplication operation.
    """
    return a * b
