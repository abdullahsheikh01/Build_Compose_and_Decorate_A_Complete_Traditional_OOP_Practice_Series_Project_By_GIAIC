#       Make a Custom Class Iterable
#       Task:
# Create a class Countdown that takes a start number.
#  Implement __iter__() and __next__() to make the object iterable in a for-loop,
#  counting down to 0.

class Countdown:
    def __init__(self,start_val:int):
        self.start_val = start_val
        self.current_val = start_val

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_val > 0:
            value = self.current_val
            self.current_val -= 1
            return value
        elif self.current_val == 0:
            value = self.current_val
            self.current_val -= 1
            return value
        else:
            raise StopIteration
        
countdown_1 : Countdown = Countdown(5)

print("Counting down from 5:")
for num in countdown_1:
    print(num)