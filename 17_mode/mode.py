def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    frequencies = {}
    for num in nums:
        if num in frequencies:
            frequencies[num] += 1
        else:
            frequencies[num] = 1
    max = 0;
    for num in frequencies.values():
        if num > 0:
            max = num
    return max


print(mode([2,2,3,3,2]))
print(mode([1,2,1]))