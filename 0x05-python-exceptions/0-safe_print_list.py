#!/usr/bin/python3
"""prints x elements of a list."""
def safe_print_list(my_list=[], x=0):
    i = 0
    written = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            written += 1
        except:
            continue
    print()
    return written
