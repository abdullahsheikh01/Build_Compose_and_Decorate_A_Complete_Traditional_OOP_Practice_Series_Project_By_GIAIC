#       Property Decorators: @property, @setter, and @deleter
#       Task:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self,name :str,price:float):
        self.name : str = name
        if price<0:
            raise ValueError("New Price Should be higher than 0")
        else:
            self.__price = price


    @property
    def price(self):
        return self.__price
    
    @price.setter
    def set_price(self,new_price):
        if new_price<0:
            raise ValueError("New Price Should be higher than 0")
        else:
            self.__price = new_price
    
    @price.deleter
    def del_price(self):
        del self.__price

# product1 : Product = Product("Watch",-552)#It cause Error
product2 : Product = Product("Watch",552)

print(product2.price)
product2.set_price = 65
# product2.set_price = -98 # Cause Error
print(product2.price)
del product2.del_price
# print(product2.price) # Cause Error