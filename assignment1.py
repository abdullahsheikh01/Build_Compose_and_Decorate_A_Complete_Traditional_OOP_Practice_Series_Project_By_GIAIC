#       Using self
#       Task:
# Create a class Student with attributes name and marks.
#  Use the self keyword to initialize these values via a constructor.
#  Add a method display() that prints student details.

from typing import NoReturn

class Student:
    def __init__(self,name:str,marks:float):
        self.name : str = name
        self.marks : float = marks

    def show_student_details(self)->NoReturn:
        print(f"\t\tStudent Details:\nName: {self.name}\nMarks: {self.marks}")

std : Student = Student("Ali",76)
std.show_student_details()