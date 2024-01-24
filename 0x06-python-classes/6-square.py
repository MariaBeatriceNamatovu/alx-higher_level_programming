#!/usr/bin/python3

"""script to print square position"""

class Square:
    """creates sqaure type"""

    def __init__(self, size=0, position=(0,0)):
        """initializes the square with position and size"""
        self.size = size
        try:
            self.position = position
        except TypeError as typ:
            print(typ)

    @property
    def position(self):
        """defines the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")


        elif type(value[0]) is not int or type(value[1]) is not int:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    @property
    def size(self):
        """defines the size of square and retruns its value"""
        return self.__size

    @size.setter
    def size(self, value):
        """defines size value"""
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise TypeError("size must be >= 0")

    def area(self):
        """defines the area of a square"""
        return self.__size * self.__size

    def my_print(self):
        """prints square by position"""
        if self.position:
            if self.size > 0:
                print('\n' * self.position[1], end="")
                for a in range(self.__size):
                    print(' ' * self.position[0], end="")
                    print('#' * self.size)
        if self.__size == 0:
            print()




