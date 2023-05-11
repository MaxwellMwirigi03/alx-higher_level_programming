#!/usr/bin/python3

"""program that prints the result of the addition of all arguments"""
if __name__ == "__main__":
    import sys

    count = len(sys.argv)
    sum = 0
    for i in range(1, count):
        sum += int(sys.argv[i])
    print(sum)
