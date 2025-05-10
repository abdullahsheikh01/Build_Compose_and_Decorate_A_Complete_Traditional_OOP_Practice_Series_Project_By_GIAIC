#       Class Variables and Class Methods
#       Task:
# Create a class Bank with a class variable bank_name.
# Add a class method change_bank_name(cls, name) that allows changing the bank name. 
# Show that it affects all instances.

class Bank:
    bank_name : str = "HBL"

    @classmethod
    def change_bank_name(cls,name:str):
        cls.bank_name = name

var1 : Bank = Bank()
var2 : Bank = Bank()
check1 : bool = var1.bank_name==var2.bank_name
print("var1.bank_name = ",var1.bank_name)
print("var2.bank_name = ",var2.bank_name)

Bank.change_bank_name("Al Habib")
check2 : bool = var1.bank_name==var2.bank_name
print("var1.bank_name = ",var1.bank_name)
print("var2.bank_name = ",var2.bank_name)