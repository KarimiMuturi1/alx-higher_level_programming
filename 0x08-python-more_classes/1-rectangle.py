#!/usr/bin/python3
"""
A module containing the class Rectangle
"""


class Rectangle:
    """
    A class Rectangle that defines a Rectangle with two properties
    The properties are it's width and height
    """
    def __init__(self, width=0, height=0):
        """
        Initializes the private attributes width and height
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        getter method for the width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        setter method for the width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        getter method for the height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        setter method for the height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
