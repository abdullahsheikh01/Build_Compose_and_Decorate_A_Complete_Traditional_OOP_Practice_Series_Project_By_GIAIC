#       Static Methods
#       Task:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that 
# returns the Fahrenheit value.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c:float):
        a : float = 9/5
        b : float = c*a
        return b+32
    
var : float = TemperatureConverter.celsius_to_fahrenheit(55.22)
print(var)