def sum_array(array):

    '''Return sum of all items in array'''

    return sum(array)

def fibonacci(n):

    """
    Calculate nth term in fibonacci sequence

    Args:
        n (int): nth term in fibonacci sequence to calculate

    Returns:
        int: nth term of fibonacci sequence,
             equal to sum of previous two terms

    Examples:
        >>> fibonacci(1)
        1
        >> fibonacci(2)
        1
        >> fibonacci(3)
        2
    """

    if n <= 1:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def factorial(n):

    '''Return n!'''
    if n == 1:
        return n
    elif n == 0:
        return 1
    else:
         return n * factorial(n-1)
     

def reverse(word):

    '''Return word in reverse'''
    reversedstring = word[::-1]
    return reversedstring
