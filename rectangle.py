"""Rectangle class is a sub class that could inherit some features from parent class shape"""
"""but adds length and width attribute, area and perimeter formulas, is_unit_circle() method and draw()
method from matplotlib"""


import numbers

import matplotlib.pyplot as plt

from shape import Shape

class Rectangle(Shape):
    def __init__(self, x=0.0, y=0.0, width=1.0, height=1.0, compare_by="area"):
        super().__init__(x, y, compare_by)
        
        self.width = width
        self.height = height


    @property
    def width(self):
        """Width of rectangle (float)."""
        return self._width

    @width.setter
    def width(self, new_width):
        if not isinstance(new_width, (numbers.Number)):
            raise TypeError("width must be a number")
        if new_width <= 0:
            raise ValueError("width must be positive")
        self._width = (new_width)

    @property
    def height(self):
        """Height of rectangle (float)."""
        return self._height

    @height.setter
    def height(self, new_height):
        if not isinstance(new_height, (numbers.Number)):
            raise TypeError("height must be a number.")
        if new_height <= 0:
            raise ValueError("height must be positive.")
        self._height =(new_height)

    @property
    def area(self):
        """read only area property(width * height)"""
        return self.width * self.height
    
    @property
    def perimeter(self):
        """read only perimeter property(2 * (width + height))"""
        return 2 * self.width * self.height
    
    def is_square(self):
        """return True if width = height"""
        return self.width == self.height
    
    def draw(self, color='green'):
        """draw rectangle centered at (x, y(0,0)) axis."""




