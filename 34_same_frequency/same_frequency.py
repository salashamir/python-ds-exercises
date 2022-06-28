def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1_list = list(str(num1))
    num2_list = list(str(num2))
    if len(num1_list) != len(num2_list):
        return False
    num1_dict = {}
    num2_dict = {}

    for val1, val2 in zip(num1_list, num2_list):
        num1_dict[val1] = num1_dict.get(val1, 0) + 1
        num2_dict[val2] = num2_dict.get(val2, 0) + 1

    return num1_dict == num2_dict


print(same_frequency(551122, 221515))
print(same_frequency(321142, 3212215))
print(same_frequency(1212, 2211))
