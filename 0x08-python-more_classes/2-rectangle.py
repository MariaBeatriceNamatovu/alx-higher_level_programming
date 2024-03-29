#!/usr/bin/python3
"""defines a rectangle class"""

class Rectangle:


    """represents a rectangle"""

    def __init__(self, width=0, height=0):
        """initilaizes a new rectangle
        Args:
            width(int): the width of the new rectangle
            height(int): the height of the new rectangle

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the rectangle width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value


    @property
    def height(self):
        """get the height of the rctangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the rectangle height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
