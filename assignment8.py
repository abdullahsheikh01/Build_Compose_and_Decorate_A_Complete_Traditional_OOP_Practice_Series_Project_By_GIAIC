#       The super() Function
#       Task:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher
#  from it, add a subject field, and use super() to call the base class constructor.

class Person:
    def __init__(self,name:str):
        self.name : str = name
    
class Teacher(Person):
    def __init__(self,name:str,subject:str):
        super().__init__(name) # Here the base class constructor calls
        self.subject : str = subject

teacher : Teacher = Teacher("Zia Khan","Artificial Intelligence")