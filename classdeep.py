'''CLASS DEEP
(1) Encapsulation
(2) Inherintance
(3) Polimorphism
'''

'''
Java C++ ==> public private protected
'''
print("======== Encapsulation ==========")
# Python ==> public __private _protected


class Account:
    # state
    description = "The class creates bank accounts"

    # constructor

    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount

    # method
    def get_balance(self):
        print(f"Holder {self.__owner} your is balance {self.__amount} usd")

    def deposit(self, amount):
        print("*** deposit executed ***")
        self.__amount += amount

    def withdraw(self, amount):
        print("*** withdraw executed ***")
        self.__amount -= amount

    @property
    def holder(self):
        return self.__owner

    @holder.setter
    def holder(self, new_owner):
        print("change with setter")
        self.__owner = new_owner

    def change_ownership(self, new_owner):
        print("You can change ownership")
        self.__owner = new_owner


my_account = Account("Kevin", 5000)

my_account.get_balance()

print("-------")

my_account.deposit(10000)
my_account.get_balance()
my_account.withdraw(3000)
my_account.get_balance()

print("-------")
my_account.__amount = 1000000
my_account.get_balance()
# my_account.__owner = "Fede"
my_account.get_balance()

# print(my_account.owner)
# print(my_account.__owner)

try:
    result = my_account.__owner
    print("result:", result)
except Exception as err:
    print("This state is not found", err)
else:
    print("Your request is done")
finally:
    print("Process is completed")


# account_owner = my_account.holder
# print("before account_owner:", account_owner)

# my_account.change_ownership("Fede")
# print("after account_owner:", my_account.holder)
print("Owner before:", my_account.holder)
my_account.holder = "Fede"  # state
print("Owner after:", my_account.holder)
