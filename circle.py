"""Circle class is a sub class that could inherit some features from parent class shape"""
"""but adds radius attribute, area and perimeter formulas, is_unit_circle() method and draw()
method from matplotlib."""

import numbers
from numbers import Number

import math
import matplotlib.pyplot as plt


from shape import Shape


class Circle(Shape):
    def __init__(self, x:Number=0.0, y:Number=0.0,radius:Number=1.0, compare_by:str="area"):
        super().__init__(x, y, compare_by)

    
        
        self.radius=radius

    @property
    def radius(self)-> Number:
        """radius of the circle"""
        return self._radius
    
    @radius.setter
    def radius(self, new_radius)-> Number:
            if not isinstance(new_radius,(numbers.Number)):
                raise TypeError("radius must be a number.")
            if new_radius < 0:
                raise ValueError("radius must be positive.")
            self._radius=(new_radius)

    
    @property
    def area(self)-> Number:
        """read only area property"""
        return math.pi * (self.radius **2)
    
    @property
    def perimeter(self)-> Number:
        """read-only perimeter property(circumference)."""
        return 2 * math.pi * self.radius
    

    
    def is_unit_circle(self)-> bool:
        """ checks if the circle is a unit circle(when radius=1 and centered at origin (0,0))"""
        return self._radius == 1 and self.x == 0 and self.y == 0
    
    def draw(self,color = 'blue'):
        """visualize and draw the circle using matplotlib."""
        fig,ax = plt.subplots()
        circle_patch= plt.Circle((self.x, self.y), self.radius, color=color, fill=False, linewidth=2)
        ax.add_patch(circle_patch)
        ax.set_aspect('equal', adjustable= 'box')
        ax.set_xlim(self.x - self.radius * 2, self.x + self.radius * 2)
        ax.set_ylim(self.y - self.radius * 2, self.y + self.radius * 2)
        ax.set_title(f"Circle at ({self.x}, {self.y} with radius{self.radius}")
        plt.grid                                                                                                                                (True)
        plt.show()

        

    def __repr__(self):
        return f"Circle(x={self.x},y={self.y}, radius={self.radius})"
    
    def __str__(self):
        """Return user-friendly string."""
        return f"Circle centered at ({self.x}, {self.y}) with radius={self.radius}"
    





