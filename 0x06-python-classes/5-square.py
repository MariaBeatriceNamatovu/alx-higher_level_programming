#!/usr/bin/python3
"""defines a square class"""
class Square:
    """
    defines a square class
    arguments:
            size(int)
    """
    def __init__(self, size=0):
        self.size=size

    @property
    def size(self):
        """to retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """defines the size of the square"""
        if isinstance(value, int):
            if value>=0:
                self.__size=value
            else:
                raise ValueError("size must be >=0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """returns the current square area"""
        return self.__size**2

    def my_print(self):
        """returns the square with '#' character"""
        if self.__size==0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)

