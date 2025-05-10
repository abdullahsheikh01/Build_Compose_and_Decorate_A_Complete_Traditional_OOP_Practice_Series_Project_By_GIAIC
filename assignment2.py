#       Using cls
#       Task:
# Create a class Counter that keeps track of how many objects have been created.
# Use a class variable and a class method with cls to manage and display the count.
class Counter:
    __count_of_object : int = 0

    def __init__(self):
        __class__.__count_of_object+=1

    @classmethod
    def show_count_of_objects(cls):
        if cls.__count_of_object:
            print(f"Total Numbers of objects created of Counter Class: {cls.__count_of_object}")
        else:
            print("There is no any object created of Counter Class")

Counter.show_count_of_objects()
var1 : Counter = Counter()
Counter.show_count_of_objects()

var2 : Counter = Counter()
Counter.show_count_of_objects()