#!/usr/bin/python3

def uppercase(str):
    for letr in str:
        a = ord(letr)
        if a >= 97 and a <= 122:
            letr = chr(ord(letr) - (ord('a') - ord('A')))
        print("{:s}".format(letr), end="")
    print("")
