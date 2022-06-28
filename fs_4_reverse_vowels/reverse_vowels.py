def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    string_list = list(s)

    indices = [idx for idx,char in enumerate(string_list) if char.lower() in 'aeiou']
    print("INDICES:", indices)

    reversed_indices = list(reversed(indices))
    print(reversed_indices)

    for idx in range(len(indices)//2):
        string_list[indices[idx]], string_list[reversed_indices[idx]] = string_list[reversed_indices[idx]], string_list[indices[idx]]

    return ''.join(string_list)


print(reverse_vowels("aeiou"))
print(reverse_vowels("Reverse Vowels In A String"))
print(reverse_vowels("why try, shy fly?"))
print(reverse_vowels("Tomatoes"))