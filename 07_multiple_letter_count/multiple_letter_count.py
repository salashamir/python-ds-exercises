def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    chars_dict = {}
    for char in phrase:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1

    return chars_dict


print(multiple_letter_count('yay'))
print(multiple_letter_count('Christmas'))
print(multiple_letter_count('Abominable'))
print(multiple_letter_count('aaabbbcccAAABBBCCC'))
