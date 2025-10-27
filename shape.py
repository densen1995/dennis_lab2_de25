#GEOMETRY: Parent class; Shape
# Shape comparison (for sub-classes;rectangle and circle, by size).
#Translation:... ..movement of the shapes(rectangle and circle from their various center position (0,0))

class Shape:
    """Parent class for the geometric shapes
    """

    """attributes x and y coordinates for the shapes """
    def __int__(self, x:int|float , y:int|float):
        self.x=x
        self.y=y


    @property
    def x(self):
        return self._x 
    
    












    def __repr__(self):
        return f"Shape(x={self.x}, y={self.y})"
    

