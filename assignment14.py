#       Composition
#       Task:
# Create a class Department and a class Employee. 
# Use aggregation by having a Department object store a reference to an Employee object 
# that exists independently of it.

class Employee:
    def __init__(self,name:str,age:int,experience : int):
        self.name : str = name
        self.age : str = age 
        self.experience : int = experience

class Department:
    def __init__(self,name:str,employee:Employee):
        self.name : str = name
        self.employee : Employee = employee
    
employee1 : Employee = Employee("Arif",29,4)
department : Department = Department("Marketing",employee1)
print(id(employee1)==id(department.employee))