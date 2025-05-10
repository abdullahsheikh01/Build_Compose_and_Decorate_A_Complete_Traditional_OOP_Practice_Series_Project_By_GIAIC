#       Access Modifiers: Public, Private, and Protected
#       Task:

class Employee:
    name : str = "Shahid"
    _salary : int = 53290
    __ssn : int = 6746558

employe1 : Employee = Employee()
print(employe1.name) # It can be accessed
print(employe1._salary) # It can also be accessed 
# print(employe1.__ssn) # It can't be accessed