'''CLASS
(1) What is class
(2) ordinary vs static properties
(3) special methods
'''

print("========= What is Class? ===========")

# Class - similar objectlarni create qilishda template
# Structure of classes ==> STATE CONSTRUCTOR METHOD


class Person():
    # state
    message = "Class State Property"

    # constructor state property
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method

    def introduce(self):
        print(f"{self.name} is {self.age}")

    @classmethod
    def explain(args):
        print("static method property executed")


person1 = Person("Kevin", 25)
person2 = Person("RYAN", 23)
person3 = Person("LEO", 22)

print(person1.name)  # ordinary state
person1.introduce()  # ordinary method

print(person2.name)
person2.introduce()


print("========= ordinaary and static properties ===========")
# static state

print(Person.message)


# static method  class decoraters bilan hosil qilinadi
Person.explain()

print("========= special/magic methods ===========")

# Python's most common used special methods:
# __init__ __new__ __str__ __call__ __getitem__ __eq__ __len__


class Car:
    # state
    description = "This class makes cars"

    # constructor

    def __new__(clc, *args):
        print("* __new__ *")
        return super().__new__(clc)

    def __init__(self, name, year):
        self.name = name
        self.year = year

    def start(self):
        print(f"{self.name} started engine")

    def stop(self):
        print(f"{self.name} stopped engine")

    def __str__(self):
        return f"This: {self.name} and was produced in {self.year}"

    def __call__(self, *args, **kwds):
        print("Object is called as a function")
        return True


my_car = Car("MERC", 2025)
my_car.start()
my_car.stop()

your_car = Car("Tayota", 2026)

print(your_car)
your_car()  # execute a sa function we use __call__ method

response = your_car()
print(response)
