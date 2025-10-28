#GEOMETRY: Parent class; Shape( represents/declares what every shape must have. )
# Shape comparison (for sub-classes;rectangle and circle, by area).
#Translation:... ..movement of the shapes(rectangle and circle from their various center position (0,0))

import math  #(built in for mathematical functions and calculations.)
import matplotlib.pyplot as py
#import pytest


class Shape:
    """Parent class for the geometric shapes
    """

    """attributes x and y coordinates for the shapes """
    def __int__(self, x , y):

        """initialize a shape with x and y cordinates and raises type error if x and y are not numeric(error check)"""

        if not isinstance (x,(int,float)) and isinstance(y,(int,float)):
            raise TypeError("x and y must be numeric values.")
        self._x=x
        self._y=y


    @property
    def x(self):
        """returns the x coordinate of the shape"""
        return self._x 
    
    @property
    def y(self):
        """returns the y coordinate of the shape"""
        return self._y
    

    def translate(self, dx, dy):
        """move the shape by dx and dy and raises type error if they are not numeric values"""
        if not isinstance (dx,(int,float)) and isinstance (dy,(int,float)):
            raise TypeError("dx and dy must be numeric values.")
        self._x+=dx #(movements occurs when a value/number assigned to dy or dx is added to the x and y instances which is set at 0,0)
        self._y+=dy


    def __eq__(self, other):
        """check equality based on area"""
        if not isinstance(other,Shape):
            return NotImplemented
        return self.area ==other.area
    
    def __lt__(self,other):
        """compare shapes by area (less than)"""
        if not isinstance(other,Shape):
            return NotImplemented
        return self.area < other.area
    
    def __le__(self,other):
        """"compare shapes by area(less than or equal )"""
        return self ==other or self < other
    
    def __gt__(self,other):
        """compare shapes by area(greater than)"""
        return not self.__le__(other)      #self.area  > other.area(this works against DRY(Do Not Repeat Yourself) principles)
    
    def __ge__(self,other):
        """compares shapes by area(less than or equal)"""
        return not self.__lt__(other)       #self.area == other or self.area > other(also works against "DRY")
    
    def __repr__(self):
        """return developer friendly and readable representaion(makes it more readable)"""
        return f"Shape(x={self.x}, y={self.y})"
    def __str__(self):
        """return user friendly and freadable representation """
        return f"Shape centered and positioned at ({self.x}, {self.y})"
    
        
    












    def __repr__(self):
        return f"Shape(x={self.x}, y={self.y})"
    

