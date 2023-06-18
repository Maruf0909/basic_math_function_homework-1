def main(a):
    '''Assign the value pi to the parametr "a". Round the result to 2 decimal places and return it.
    
    Args:
        a (float): a number
        
    Returns:
        float: the result.
    '''
    from math import pi
    a = pi
    result = round(a, 2)
    return result
print(main(45))