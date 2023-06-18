def main(a, b):
    '''find the absolute value of the difference between a and b. Return it.
    
    Args:
        a (int): a number
        b (int): a number
        
    Returns:
        int: the result.
    '''
    value = a - b
    result = abs(value)
    return result
print(main(9, 11))