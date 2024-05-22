#!/usr/bin/python3

"""
    Function divides all elements of a matrix

    Example:
       a = 5
       b = 10

       add_integer(a, b)

       15
"""

def add_integer(a, b=98):
    """
        Args:
            a: first integer
            b: second integer

        Returns:
            Sum of the two integers
    """
    result = 0

     if not isinstance(a, (float, int)):
        if a is not None:
            raise TypeError("a must be an integer")
        raise ValueError("a must be an integer")

    if not isinstance(b, (float, int)):
        if b is not None:
            raise TypeError("b must be an integer")
        raise ValueError("b must be an integer")

    if type(a) is float and type(b) is float:
        return int(a) + int(b)

    elif type(a) is not float and type(b) is float:
        return a + int(b)

    elif type(a) is float and type(b) is not float:
        return int(a) + b

    return a + b
