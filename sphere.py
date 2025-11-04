"""Sphere class is a sub class that could inherit some features from parent class shape"""
"""but adds radius attribute, area ,perimeter and volume formulas, is_unit_sphere() method and draw()
method from matplotlib."""
import numbers
import math
import matplotlib.pyplot as plt
from shape import Shape


class Sphere (Shape):
    """a 3D sphere shape """
    def __init__(self, x=0, y=0, z=0, radius=1, compare_by= "area"):
        super().__init__(x,y,z, compare_by)

        """validate radius<"""
        if not isinstance(radius, (numbers.Number)):
            raise TypeError("radius must be numeric")
        if radius <= 0:
            raise ValueError("radius must be positive")
        
        
        self.radius = radius

    @property
    def radius(self):
        return self._radius
    
    """validate radius"""
    @radius.setter
    def radius(self, value):
        if not isinstance(value, (numbers.Number)):
            raise TypeError("radius must be numeric")
        if value <= 0:
            raise ValueError("radius must be positive")
        self._radius=value
        
    

    @property
    def area(self):
        """read-only """
        return 4 * math.pi * (self._radius ** 2)
    
    @property
    def perimeter(self):
        return 2 * math.pi * self._radius
    
    @property
    def perimeter(self):
        return 2 * math.pi * self._radius #could also be circumference
    
    @property
    def volume(self):
        return (4/3) * math.pi * (self._radius ** 3)
    
    def is_unit_sphere(self):
        return self._radius == 1
    
    
    

    


    def __repr__(self):
        return f"Sphere(x={self._x}, y={self._y}, z={self._z}, radius={self._radius})"

    def __str__(self):
        return f"Sphere centered at ({self._x}, {self._y}, {self._z}) with radius {self._radius})"
    
    
    
     




