"""Optional questions for Lab 1"""

# While Loops


def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    if k == 0:
        return 1

    falling_k = k
    falling_n = n
    factorial = 1
    while (falling_k > 0):
        factorial *= falling_n
        falling_n = falling_n - 1
        falling_k = falling_k - 1

    return factorial


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    if (n > 10):
        divied_n = n
        while (divied_n > 0):
            first_digit = divied_n % 10
            second_digit = divied_n // 10 % 10
            if (first_digit == second_digit == 8):
                return True
            divied_n = divied_n // 10

    return False
