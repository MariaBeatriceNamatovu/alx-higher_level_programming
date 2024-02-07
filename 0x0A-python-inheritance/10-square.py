#!/usr/bin/python3
"""Defines a class Rectangle subclass Square"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size):
        """
        initialize a new Rectangle
        Args:
            width (int): The width of the new Rectangle
            height (int): The height of the new Rectangle
        """

        super().integer.validator("size", size)
        super().__init__(size, size)
        self.__size = size

