#!/usr/bin/python3

"""Prints the alphabet in reverse and alternates upper and lower cases."""
for num in range(122, 96, -1):
    if num % 2:
        num = num - 32
    print("{:c}".format(num), end="")
