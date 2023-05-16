#!/usr/bin/python3

def no_c(my_string):
    """Function that removes all characters c and C from a string."""
    newstr = ''
    for x in my_string:
        if x != 'c' and x != 'C':
            newstr += x
    return newstr
