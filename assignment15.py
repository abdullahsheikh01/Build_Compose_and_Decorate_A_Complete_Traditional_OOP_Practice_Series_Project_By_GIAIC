#       Method Resolution Order (MRO) and Diamond Inheritance
#       Task:
""" Create four classes:

A with a method show(),

B and C that inherit from A and override show(),

D that inherits from both B and C.

Create an object of D and call show() to observe MRO."""

class A:
    @staticmethod
    def show():
        print("This is show message of Class A")

class B(A):
    @staticmethod
    def show():
        print("This is show message of Class B")

class C(A):
    @staticmethod
    def show():
        print("This is show message of Class C")

class D(B,C):
    pass

d : D = D()
D.show()