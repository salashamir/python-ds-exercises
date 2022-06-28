def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    swapped_phrase = []
    for char in phrase:
        if char == to_swap.upper():
            swapped_phrase.append(char.lower())
        elif char == to_swap.lower():
            swapped_phrase.append(char.upper())
        else:
            swapped_phrase.append(char)

    return ''.join(swapped_phrase)


print(flip_case('Aaaahhh', 'a'))
print(flip_case('Aaaahhh', 'A'))
print(flip_case('Aaaahhh', 'h'))