#       Instance Methods
#       Task:
# Create a class Dog with instance variables name and breed. 
# Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self,name:str,breed:str):
        self.name : str = name
        self.breed : str = breed

    def bark(self):
        print(f'{self.name} barked loudly, "Woof! Woof!"')

dog1 : Dog = Dog("Max","Golden Retriever")
dog1.bark()