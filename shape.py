#GEOMETRY: Parent class; Shape( represents/declares what every shape must have. )
# Shape comparison (for sub-classes;rectangle and circle, by area or perimeter).
#Translation:... ...movement of the shapes(rectangle and circle from their various center position (0,0))

  



import numbers
from numbers import Number

class Shape:
    """Parent class for the geometric shapes
    """

    """attributes x and y coordinates for the shapes  """
    """attributes z( optional height cordinates used by 3D shapes.)"""
    """attribute compare_by setting for comparison framework"""
    def __init__(self, x:Number=0 , y:Number=0, compare_by:str="area" ):

        """initialize a shape with x and y cordinates and raises type error if x ,y and z are not numeric(error check)"""
        """initialize a shape that compares defauultly by area or manually by perimeter"""

        if not isinstance(x, (numbers.Number)) or not isinstance(y, (numbers.Number)):
            raise TypeError("x and y must be numeric values.")
        
        
         
        self._x=x
        self._y=y
        
        self._compare_by= compare_by


    @property
    def x(self) -> Number:
        """returns the x coordinate of the shape"""
        return self._x 
    
    @property
    def y(self) -> Number:
        """returns the y coordinate of the shape"""
        return self._y
    
    
    @property
    def compare_by(self) -> str:
        """comparison , by either area or perimeter or volume ."""
        return self._compare_by
    
    @compare_by.setter
    def compare_by(self, value: Number):
        if value not in ("area", "perimeter", "volume"):
            raise ValueError("compare_by must be 'area' or 'perimeter' or 'volume' ")
        self._compare_by = value

    
    @property
    def area(self)->Number:
        return self._area
    
    @property
    def perimeter(self)->Number:
        return self._perimeter
    
    @property
    def volume(self)->Number:
        return self._volume
    

    def translate(self, dx, dy) -> None:
        """move the shape by dx ,dy and dz(if 3D) raises type error if they are not numeric values"""
        if not isinstance (dx,(numbers.Number)) and isinstance (dy,(numbers.Number)) :
            raise TypeError("dx, and dy  must be numeric values.")
        
        self._x+=dx #(movements occurs when a value/number assigned to dy or dx is added to the x and y instances which is set at 0,0)
        self._y+=dy   #the value of x  and add to thereself respectively once a movement has been made.  
       
        """comparison method to compare by area or shape"""
    def compare_value(self)->Number:
        """return the value used for comparison"""
        return self.area if self.compare_by=="area" else self.perimeter or self.volume


    def __eq__(self, other: "Shape")->bool:
        """check equality based on area or perimeter or volume"""
        if not isinstance(other,Shape):
            return NotImplemented
        return self.compare_value()== other.compare_value()
    
    def __lt__(self,other)->bool:
        """compare shapes by area or perimeter or volume  (less than)"""
        if not isinstance(other,Shape):
            return NotImplemented
        return self.compare_value() < other.compare_value()
    
    def __le__(self,other)->bool:
        """"compare shapes by area or perimeter or volume (less than or equal )"""
        if not isinstance(other, Shape):
            return NotImplemented
        return self.compare_value() <= other.compare_value()
    
    def __gt__(self,other)->bool:
        """compare shapes by area or perimeter or volume(greater than)"""
        return not self.__le__(other) #self.compare_value()>other._compare_value()(this works against DRY(Do Not Repeat Yourself) principles)
    
    def __ge__(self,other)->bool:
        """compares shapes by area or perimeter or volume (less than or equal)"""
        return not self.__lt__(other) #self.compare_value() >= other.compare_value() (but also works against "DRY")
    
    def __repr__(self)->str:
        """return developer friendly and readable representaion(makes it more readable)"""
        return f"Shape(x={self.x}, y={self.y}, compare_by={self.compare_by})"
    def __str__(self)->str:
        """return user friendly and readable representation """
        return f"Shape centered and positioned at ({self.x}, {self.y},)"
    

