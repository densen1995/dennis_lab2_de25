"""Sphere class is a sub class that could inherit some features from parent class shape"""
"""but adds radius attribute, area ,perimeter and volume formulas, is_unit_sphere() method and draw()
method from matplotlib."""
import numbers
from numbers import Number
import math
import matplotlib.pyplot as plt
from shape import Shape


class Sphere (Shape):
    """a 3D sphere shape """
    def __init__(self, x:Number=0, y:Number=0, z:Number=0, radius:Number=1, compare_by:str= "area"):
        super().__init__(x,y, compare_by)

        """validate radius<"""
        if not isinstance(radius, (numbers.Number)):
            raise TypeError("radius must be numeric")
        if radius <= 0:
            raise ValueError("radius must be positive")
        
        
        self.radius = radius
        self._z = z
    @property
    def z(self)->Number:
        return self._z
    

    @property
    def radius(self)->Number:
        return self._radius
    
    """validate radius"""
    @radius.setter
    def radius(self, value)->Number:
        if not isinstance(value, (numbers.Number)):
            raise TypeError("radius must be numeric")
        if value <= 0:
            raise ValueError("radius must be positive")
        self._radius=value
        
    

    @property
    def area(self)->Number:
        """read-only """
        return 4 * math.pi * (self._radius ** 2)
    
    @property
    def circumference(self)->Number:
        return 2 * math.pi * self._radius

    
    @property
    def volume(self)->Number:
        return (4/3) * math.pi * (self._radius ** 3)
    

    

    def translate(self, dx, dy, dz)->None:
        print(f" move the cordinates by (x+= {dx}), x+={dy} , x+={dz}")


        # Validate inputs
        for val, name in zip((dx, dy, dz), ("dx", "dy", "dz")):
            if not isinstance(val, (int, float)):
                raise TypeError(f"{name} must be a number.")

        # Move the x and y coordinates using the parent method (Shape handles 2D)
        super().translate(dx, dy)

    # Move z coordinate separately (added in 3D shapes)
        self._z += dz

        print(f"Moved shape by (x+={dx}, y+={dy}, z+={dz})")
        print(f"New position: ({self._x}, {self._y}, {self._z})")
    
    def is_unit_sphere(self)->bool:
        return self._radius == 1
    
    
    

    


    def __repr__(self):
        return f"Sphere(x={self._x}, y={self._y}, z={self._z}, radius={self._radius})"

    def __str__(self):
        return f"Sphere centered at ({self._x}, {self._y}, {self._z}) with radius {self._radius})"
    
    
    
     




