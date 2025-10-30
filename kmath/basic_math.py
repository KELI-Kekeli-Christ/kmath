def multiply(num_1=1,num_2=1,start=1,end=1):
    result=num_1*num_2
    if end>1:
        for i in range(start,end+1):
            result*=i
        return result
    return result

multiply.__doc__="""
Multiplies two numbers and optionally multiplies by a range of integers.   
Parameters:
- num_1 (int, float): The first number to multiply. Default is 1
- num_2 (int, float): The second number to multiply. Default is 1
- start (int): The starting integer of the range to multiply. Default is 1
- end (int): The ending integer of the range to multiply. Default is 1
Returns:
- int, float: The result of the multiplication.
Example:
- multiply(2, 3) returns 6
- multiply(2, 3, 1, 4) returns 144 (2
* 3 * 1 * 2 * 3 * 4)
"""




def divide(num_1=1, num_2=1, start=1, end=1):
    """
    Divides num_1 by num_2 and optionally divides by each integer in range(start, end).
    Raises ZeroDivisionError on division by zero.
    example:
    - divide(8, 2) returns 4.0
    - divide(8, 2, 1, 4) returns 0.041666666666666664 (8 / 2 / 1 / 2 / 3 / 4)
    Parameters:
    - num_1 (int, float): The numerator. Default is 1.
    - num_2 (int, float): The denominator. Default is 1.
    - start (int): The starting integer of the range to divide. Default is 1.
    - end (int): The ending integer of the range to divide. Default is 1.
    Returns:
    - float: The result of the division.
    """
    if num_2 == 0:
        raise ZeroDivisionError("division by zero")
    result = num_1 / num_2
    if end > 1:
        for i in range(start, end + 1):
            if i == 0:
                raise ZeroDivisionError("division by zero in range")
            result /= i
    return result