#       Public Variables and Methods
#       Task:
# Create a class Car with a public variable brand and a public method start().
#  Instantiate the class and access both from outside the class.

class Car:
    brand : str = "Toyota"

    @staticmethod
    def start():
        print("Car Started...")

car1 : Car = Car()
print(car1.brand)
car1.start()