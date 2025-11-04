"""Cube class is a sub class that could inherit some features from parent class shape"""
"""but adds side attribute, area ,perimeter and volume formulas, is_unit_cube() method and draw()
method from matplotlib."""
import numbers
import math
import matplotlib.pyplot as plt
from shape import Shape

class Cube(Shape):
    """3D cube shape"""

    def __init__(self, x=0, y=0, z=0, side=1, compare_by="area"):
        super().__init__(x, y, z, compare_by)

        self.side=side

       


    @property
    def side(self):
        return self._side
    
    """validate side"""
    @side.setter
    def side(self,value):
        if not isinstance(value, (numbers.Number)):
            raise TypeError("side must be a numeric value")
        if value <=0:
            raise ValueError("side must be positive")
        self._side = value

    @property
    def area(self):
        return 6 * (self._side ** 2 )
    
    @property
    def perimeter(self):
        return 12 * self._side 
    
    @property
    def volume(self):
        return self._side ** 3
    
    def is_unit_cube(self):
        return self._side == 1
    


    def __repr__(self):
        """Developer-friendly string representation."""
        return f"Cube(x={self._x}, y={self._y}, z={self._z}, side={self._side})"

    def __str__(self):
        """User-friendly string representation."""
        return f"Cube centered at ({self._x}, {self._y}, {self._z}) with side length {self._side}"