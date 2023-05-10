#!/usr/bin/python3

def print_last_digit(number):
    """Print the last digit of a number and return it"""
    if number >= 0:
        print("{:d}".format(number % 10), end="")
        return number % 10
    else:
        print("{:d}".format((number * -1) % 10), end="")
        return (number * -1) % 10
