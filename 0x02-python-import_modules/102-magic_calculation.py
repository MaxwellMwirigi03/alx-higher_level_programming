#!/usr/bin/python3

""" Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode provided"""
def magic_calculation(a, b):
    """Match bytecode provided by Holberton School."""
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return (c)

    else:
        return (sub(a, b))
