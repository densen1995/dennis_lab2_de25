"""Cube class is a sub class that could inherit some features from parent class shape"""
"""but adds side and z(for 3D shapes)attribute, area ,perimeter and volume formulas, is_unit_cube() method ."""
import numbers
from numbers import Number

from shape import Shape

class Cube(Shape):
    """3D cube shape"""

    def __init__(self, x:Number=0, y:Number=0, z:Number=0, side:Number=1, compare_by:Number="area"):
        super().__init__(x, y, compare_by)

        self.side=side
        self._z=z

       
    @property
    def z(self)->Number:
        return self._z

    @property
    def side(self)->Number:
        return self._side
    
    """validate side"""
    @side.setter
    def side(self,value)->Number:
        if not isinstance(value, (numbers.Number)):
            raise TypeError("side must be a numeric value")
        if value <=0:
            raise ValueError("side must be positive")
        self._side = value

    @property
    def area(self)->Number:
        return 6 * (self._side ** 2 )
    
    @property
    def perimeter(self)->Number:
        return 12 * self._side 
    
    @property
    def volume(self)->Number:
        return self._side ** 3
    
    def translate(self, dx, dy, dz)->None:
        print(f" move the cordinates by (x+= {dx}), x+={dy} , x+={dz}")


        # Validate inputs
        for val, name in zip((dx, dy, dz), ("dx", "dy", "dz")):
            if not isinstance(val, (numbers.Number)):
                raise TypeError(f"{name} must be a number.")

        # Move the x and y coordinates using the parent method (Shape handles 2D)
        super().translate(dx, dy)

    # Move z coordinate separately (added in 3D shapes)
        self._z += dz

        print(f"Moved shape by (x+={dx}, y+={dy}, z+={dz})")
        print(f"New position: ({self._x}, {self._y}, {self._z})")

    def compare_value(self):
        return self.area if self.compare_by == "area" else self.volume
    
    def is_unit_cube(self)->bool:
        return self._side == 1
    


    def __repr__(self):
        """Developer-friendly string representation."""
        return f"Cube(x={self._x}, y={self._y}, z={self._z}, side={self._side})"

    def __str__(self):
        """User-friendly string representation."""
        return f"Cube centered at ({self._x}, {self._y}, {self._z}) with side length {self._side}"