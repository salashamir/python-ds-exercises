def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    processed_phrase = phrase.lower().replace(' ','')
    if processed_phrase == processed_phrase[::-1]:
        return True
    return False


print(is_palindrome('taco cat'))
print(is_palindrome('highway'))
print(is_palindrome('Noon'))
