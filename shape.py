#GEOMETRY: Parent class; Shape( represents/declares what every shape must have. )
# Shape comparison (for sub-classes;rectangle and circle, by area or perimeter).
#Translation:... ...movement of the shapes(rectangle and circle from their various center position (0,0))

  



import numbers
class Shape:
    """Parent class for the geometric shapes
    """

    """attributes x and y coordinates for the shapes  """
    """attribute compare_by setting for comparison framework"""
    def __init__(self, x=0 , y=0, compare_by="area"):

        """initialize a shape with x and y cordinates and raises type error if x and y are not numeric(error check)"""
        """initialize a shape that compares defauultly by area or manually by perimeter"""

        if not isinstance (x,(numbers.Number)) or not isinstance(y,(numbers.Number)):
            raise TypeError("x and y must be numeric values.")
        
        
         
        self._x=x
        self._y=y
        self._compare_by=compare_by


    @property
    def x(self):
        """returns the x coordinate of the shape"""
        return self._x 
    
    @property
    def y(self):
        """returns the y coordinate of the shape"""
        return self._y
    
    @property
    def compare_by(self):
        """comparison , by either area or perimeter"""
        return self._compare_by
    
    @compare_by.setter
    def compare_by(self, value):
        if value not in ("area", "perimeter"):
            raise ValueError("compare_by must be 'area' or 'perimeter'")
        self._compare_by = value

    
    @property
    def area(self):
        return self._area
    
    @property
    def perimeter(self):
        return self._perimeter
    

    def translate(self, dx, dy):
        """move the shape by dx and dy and raises type error if they are not numeric values"""
        if not isinstance (dx,(numbers.Number)) and isinstance (dy,(numbers.Number)):
            raise TypeError("dx and dy must be numeric values.")
        self._x+=dx #(movements occurs when a value/number assigned to dy or dx is added to the x and y instances which is set at 0,0)
        self._y+=dy

        """comparison method to compare by area or shape"""
    def compare_value(self):
        """return the value used for comparison"""
        return self.area if self.compare_by=="area" else self.perimeter


    def __eq__(self, other):
        """check equality based on area or perimeter"""
        if not isinstance(other,Shape):
            return NotImplemented
        return self.compare_value()== other.compare_value()
    
    def __lt__(self,other):
        """compare shapes by area or perimeter (less than)"""
        if not isinstance(other,Shape):
            return NotImplemented
        return self.compare_value() < other.compare_value()
    
    def __le__(self,other):
        """"compare shapes by area or perimeter(less than or equal )"""
        if not isinstance(other, Shape):
            return NotImplemented
        return self.compare_value() <= other.compare_value()
    
    def __gt__(self,other):
        """compare shapes by area or perimeter(greater than)"""
        return not self.__le__(other) #self.compare_value()>other._compare_value()(this works against DRY(Do Not Repeat Yourself) principles)
    
    def __ge__(self,other):
        """compares shapes by area or perimeter(less than or equal)"""
        return not self.__lt__(other) #self.compare_value() >= other.compare_value() (but also works against "DRY")
    
    def __repr__(self):
        """return developer friendly and readable representaion(makes it more readable)"""
        return f"Shape(x={self.x}, y={self.y}, compare_by={self.compare_by})"
    def __str__(self):
        """return user friendly and readable representation """
        return f"Shape centered and positioned at ({self.x}, {self.y})"
    
        
    












    def __repr__(self):
        return f"Shape(x={self.x}, y={self.y})"
    

