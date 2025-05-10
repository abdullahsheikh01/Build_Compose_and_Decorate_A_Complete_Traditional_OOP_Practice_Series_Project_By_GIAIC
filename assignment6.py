#       Static Variables and Static Methods
#       Task:
# Create a class Logger that prints a message when an object is created (constructor)
# and another message when it is destroyed (destructor).

class Logger:
    def __init__(self):
        print("Object is Created")
    
    def __del__(self):
        print("Object is deleted")
    
logger1 : Logger = Logger()
del logger1