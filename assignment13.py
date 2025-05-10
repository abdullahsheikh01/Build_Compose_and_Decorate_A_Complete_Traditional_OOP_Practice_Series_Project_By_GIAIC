#       Composition
#       Task:
# Create a class Engine and a class Car. 
# Use composition by passing an Engine object to the Car class during initialization. 
# Access a method of the Engine class via the Car class.

class Engine:
    company : str = "BMW AG"
    @staticmethod
    def start():
        print("Engine Started...")

class Car:
    def __init__(self,car_name:str,color:str):
        self.car_name : str = car_name
        self.engine : str = Engine()
        self.color : str = color
    
car1 : Car = Car("BMW Z4","Black")
car1.engine.start()