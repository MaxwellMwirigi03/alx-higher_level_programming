#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number
number = digit % 10
if digit < 0:
    digit = digit * -1
    number = (digit % 10) * -1
    digit = digit * -1
if number > 5:
    print(f"Last digit of {digit} is {number} and is greater than 5")
elif number == 0:
    print(f"Last digit of {digit} is {number} and is 0")
else:
    print(f"Last digit of {digit} is {number} and is less than 6 and not 0")
