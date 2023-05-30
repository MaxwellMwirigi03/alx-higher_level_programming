#!/usr/bin/python3


class Square:
    """
    class square that has attributes:
        size: size of a side of a square
    """
    def __init__(self, size=None):
        """
        the initialization function for the square class
	Args:
	    size: size of side of a square
	Returns: None
        """
        self.__size = size
