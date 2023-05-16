#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """Function that adds 2 tuples."""
    if type(tuple_a) == int:
        tuple_a = (tuple_a, 0)
    if type(tuple_b) == int:
        tuple_b = (tuple_b, 0)
    if (len(tuple_a) == 0):
        tuple_a = (0, 0)
    if (len(tuple_a) == 1):
        tuple_a = (tuple_a[0], 0)
    if (len(tuple_b) == 0):
        tuple_b = (0, 0)
    if (len(tuple_b) == 1):
        tuple_b = (tuple_b[0], 0)
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])