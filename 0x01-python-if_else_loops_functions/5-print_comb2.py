#!/usr/bin/python3
for number in range(0, 100):
    if number == 99:
        print(f"{:d}".format(number))
    else:
        print(f"{:02d}".format(number), end=", ")
