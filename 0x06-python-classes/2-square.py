#!/usr/bin/python3

"""Define a class square"""

class Square:
    """
    A class that defines a square by 
    the private attribute size
    """

    def __init__(self, size=0):
        """Initialzies a new square.
        the arguments are the size of the square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size


