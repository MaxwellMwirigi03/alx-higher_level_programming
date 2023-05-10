#!/usr/bin/python3

def remove_char_at(str, n):
    """Create a copy of the string without the character at position n."""
    if n < 0:
        return str
    else:
        new_n = str[:n] + str[n+1:]
    return new_n
