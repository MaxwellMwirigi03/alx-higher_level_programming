#!/usr/bin/python3

def fizzbuzz():
    """Prints 1 to 100.
    Multiples of 3 print fizz
    Multiples of 5 print buzz
    Multiples of both print fizzbuzz"""
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz ", end='')
        elif i % 3 == 0:
            print("Fizz ", end='')
        elif i % 5 == 0:
            print("Buzz ", end='')
        else:
            print("{} ".format(i), end='')
