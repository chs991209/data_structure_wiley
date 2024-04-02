# R-1.1
def is_multiple(n, m):
    """
    Determine if one integer is a multiple of another.

    Args:
        n (int): The integer to be checked for being a multiple.
        m (int): The integer to check against for being a factor.

    Returns:
        bool or str: True if n is a multiple of m, False otherwise. If n equals 2 * m,
                     it returns True. If n is divisible by m, it returns 'n = mi'.
                     Otherwise, it returns False.

    Examples:
        >>> is_multiple(10, 5)
        True

        >>> is_multiple(15, 5)
        'n = mi'

        >>> is_multiple(7, 3)
        False
    """
    if n == 2 * m:
        return True
    elif n % m == 0:
        return 'n = mi'
    else:
        return False


# R 1-2
def is_even(k):
    """
    Determine if an integer is even without using multiplication, modulo, or division operators.

    Args:
        k (int): An integer value.

    Returns:
        bool: True if k is even, False otherwise.

    Raises:
        None

    Examples:
        >>> is_even(4)
        True
        >>> is_even(7)
        False
        >>> is_even(-2)
        True
    """
    k = abs(k)
    while k > 1:
        k -= 2

    return not k & 1

# R-1.3
def minmax(data):
    """
    Find the smallest and largest numbers in a sequence.

    Args:
        data (sequence): A sequence of numbers.

    Returns:
        tuple: A tuple containing the smallest and largest numbers found in the sequence.

    Raises:
        IndexError: If the sequence is empty.

    Examples:
        >>> minmax([4, 2, 7, 5, 3])
        (2, 7)
        >>> minmax([-1, 0, 5])
        (-1, 5)
        >>> minmax([3])
        (3, 3)
    """
    if len(data) == 1:
        return data[0], data[0]

    min_val = max_val = data[0]
    for num in data[1:]:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num

    return min_val, max_val


# R-1.4

def sum_of_squares(n):
    """
    Calculate the sum of the squares of all positive integers smaller than n.

    Args:
        n (int): A positive integer.

    Returns:
        int: The sum of the squares of all positive integers smaller than n.

    Raises:
        None

    Examples:
        >>> sum_of_squares(4)
        14  # 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14
        >>> sum_of_squares(1)
        0   # No positive integers smaller than 1
        >>> sum_of_squares(6)
        55  # 1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 1 + 4 + 9 + 16 + 25 = 55

    Modification History:
        - Version 1.0 (Initial implementation)
        - Version 1.1 (Optimized implementation using formula for sum of squares)
            Changed implementation to use a formula for efficiency.
    """
    return (n - 1) * n * (2 * n - 1) // 6
