#!/usr/bin/python3

"""defines a class square"""
class Square:
    """Defines a square with a private size"""
    def __init__(self, size=0):
        if isinstance(size, int):
            if size>=0:
                self.__size=size
            else:
                raise ValueError("Size must be >=0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Returns the current square  area"""
        return self.__size**2
