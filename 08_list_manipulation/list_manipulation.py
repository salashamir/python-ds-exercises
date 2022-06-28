def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """
    if command.lower() not in ["add","remove"]:
        return None
    if location.lower() not in ["beginning","end"]:
        return None
    if command.lower() == "add" and value == None:
        return None

    if command.lower() == "add":
        if location.lower() == "beginning":
            lst.insert(0, value)
        else:
            lst.append(value)
        return lst

    if command.lower() == "remove":
        if location.lower() == "beginning":
            removed_item = lst[0]
            lst.remove(removed_item)
            return removed_item
        else:
            return lst.pop()


lst = [1, 2, 3]
# print(list_manipulation(lst, 'remove', 'end'))
# print(list_manipulation(lst, 'remove', 'beginning'))
# print(lst)

print(list_manipulation(lst, 'add', 'beginning', 20))
print(list_manipulation(lst, 'add', 'end', 30))
print(lst)

print(list_manipulation(lst, 'foo', 'end') is None)
print(list_manipulation(lst, 'add', 'dunno') is None)
    