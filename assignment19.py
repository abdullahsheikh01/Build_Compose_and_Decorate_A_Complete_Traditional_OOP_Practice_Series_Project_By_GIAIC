#       callable() and __call__()
#       Task:
# Create a class Multiplier with an __init__() to set a factor. 
# Define a __call__() method that multiplies an input by the factor. 
# Test it with callable() and by calling the object like a function.
class Multiplier:
    def __init__(self,factor : float):
        self.factor : float = factor
    
    def __call__(self,input:float):
        return self.factor * input

mult1 : Multiplier = Multiplier(88.7)

result : float = mult1(5)

print("Result: ",result)