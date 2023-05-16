#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """function that prints all integers of a list, in reverse order."""
    if not my_list:
        return
    LST = my_list[:]
    lST.reverse()
    for x in LST:
        print('{:d}'.format(x))
