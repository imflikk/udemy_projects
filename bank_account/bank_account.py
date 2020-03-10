#!/bin/python3

################
# 
# Practice for working with Object-Oriented programming
# 
################

class Bank_Account:
    """Generic bank account object with basic methods."""

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def update_balance(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Bank_Account):
    """This class generates a checking account object, inheriting from Bank_Account."""

    type = "checking"

    def __init__(self, filepath, fee):
        Bank_Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee



checking = Checking('balance.txt', 1)
checking.transfer(100)
print(checking.balance)
checking.withdraw(50)
print(checking.balance)
checking.update_balance()
print(checking.type)