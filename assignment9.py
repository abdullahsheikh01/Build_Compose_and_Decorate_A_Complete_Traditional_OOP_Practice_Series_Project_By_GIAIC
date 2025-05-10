#       Abstract Classes and Methods
#       Task:
# Use the abc module to create an abstract class Shape with an abstract method area().
# Inherit a class Rectangle that implements area().

from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,height:float,width:float):
        self.height : int = height
        self.width : int = width
    def area(self):
        return self.height * self.width
    
rectangle1 : Rectangle = Rectangle(4,6.86)
area : float = rectangle1.area()
print(area)