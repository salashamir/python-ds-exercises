def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    falsy_values_removed = [item for item in lst if item]
    return falsy_values_removed


print(compact([0,1,2,'',[],False,(),None, 'All Done']))