#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Function that finds all multiples of 2 in a list."""
    LST = my_list[:]
    for i in range(len(LST)):
        if LST[i] % 2 == 0:
            LST[i] = True
        else:
            LST[i] = False
    return LST
