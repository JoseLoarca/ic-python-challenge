def extract_even_integers(integers):
    """
    Extracts even integers from a list of integers. Is 0 an even integer?
    :param integers:
    :return:
    """
    return [x for x in integers if (lambda x: x % 2 == 0)(x)]
