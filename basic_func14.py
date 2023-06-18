def main(a, b):
    '''find the floor division of a and b and return it.
    
    Args:
        a (int): a number
        b (int): a number
        
    Returns:
        int: the result.
    '''
    from math import floor
    div = a / b
    result = floor(div)

    return result
print(main(25, 2))