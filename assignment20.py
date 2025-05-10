#       Creating a Custom Exception
#       Task:
# Create a custom exception InvalidAgeError.
# Write a function check_age(age) that raises this exception if age < 18. Handle it 
# with try...except

class InvalidAgeError(Exception):
    def __init__(self,req_age:int):
        super().__init__(f"Age less than {req_age}!")

def check_age(age:int):
    if age<0:
        raise ValueError("Age can't be less than 0")
    elif age<18:
        raise InvalidAgeError(18)
    else:
        print("Yes you are adult")



def checking_func(num:int):
    try:
        check_age(num)
    except InvalidAgeError as e:
        print(f"Invalid Age Error: {e}")
    except ValueError as e:
        print(e)

for num in [22,3,-7]:
    checking_func(num)
