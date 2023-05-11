#!/usr/bin/python3

""" program that prints the number of and the list of its arguments."""
if __name__ == "__main__":
    import sys

    count = len(sys.argv)
    if count == 1:
        print("0 arguments.")
    elif count == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(count - 1))
        for i in range(1, count):
            print("{}: {}".format(i, sys.argv[i]))
