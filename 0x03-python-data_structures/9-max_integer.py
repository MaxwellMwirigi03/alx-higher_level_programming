#!/usr/bin/python3

def max_integer(my_list=[]):
    """Function that finds the biggest integer of a list."""
    if len(my_list) == 0:
        return None
    big_int = my_list[0]
    for x in my_list:
        if x > big_int:
            big_int = x
    return big_int
