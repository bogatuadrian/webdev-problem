from example import *


def functor(arg, function_list):
    """functor(integer, list of functions) -> list of integers

    Return a list containing the results of each function call with the given
    integer as argument
    """
    results = []
    for f in function_list:
        results.append(f(arg))

    return results


if __name__ == '__main__':
    print functor(3, [multiply_by_five, add_one, subtract_three])

    print functor(123, [add_one])

    # call with no functions given as parameter; returns as expected
    print functor(10, []) # => []


