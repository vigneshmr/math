from random import randrange


def addition():
    return _gen_pair(2, 6)


def subtraction():
    return _gen_pair(2, 6)


def multiplication():
    return _gen_pair(2, 3)


def squaring():
    return _gen_single(2, 3)


def _gen_pair(min_digits, max_digits):
    """
    gen_pair generates two numbers with the same number of digits
    :return: a pair of numbers. the first one is always >= the second one
    """
    n_digits = randrange(min_digits, max_digits + 1)
    a = randrange(10 ** (n_digits - 1), 10 ** n_digits - 1)
    b = randrange(10 ** (n_digits - 1), 10 ** n_digits - 1)
    if a > b:
        return a, b
    return b, a


def _gen_single(min_digits, max_digits):
    n_digits = randrange(min_digits, max_digits + 1)
    num = randrange(10 ** (n_digits - 1), 10 ** n_digits - 1)
    return num
