def find_first_element(dictionaries):
    """
    Find the first element in a list of dictionaries whose attribute x = 5
    :param dictionaries: list of dictionaries
    :return: the first dict whose x attr is 5 or an empty dict if not found
    """
    return next((d for d in dictionaries if d['x'] == 5), {})
