'''OBJECTS
(1) What is object
(2) Iterable objects and RANGE
(3) DICTIONARY
(4) Error handling system
'''

import array  # package/module
from math import ceil, asin
import math
print("====== What is object? =======")
# Object has state and method properties
# Everything is object in Python!


print(type("Hello"))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# Paradigms ==> Functional programming and OOP
# OOB 4 concepts ==> Abstraction | Encapsulation | Inherintance | Polimorphism

res1 = math.ceil(33.6)  # CALL
print(res1)

res2 = ceil(88.6)
print(res2)


print("====== Error handling system =======")


car_dict = dict(name="MERC", year=2027, elctric=True)

# try:
#     print("passed here")
#     result = car_dict["origin"]
#     print("result", result)
# except KeyError as err:
#     print("state is not found:", err)
# else:
#     print("Executed succeed without errors")
# finally:
#     print("Final step")
# print("==============")
# try:
#     print("passed here")
#     result = car_dict["year"]
#     print("result", result)
# except KeyError as err:
#     print("state is not found:", err)
# else:
#     print("Executed succeed without errors")
# finally:
#     print("Final step")

print("==============")

try:
    print("passed here")
    # a = car_dict.speed
    result = car_dict["year"]
    print("result", result)
except KeyError as err:
    print("state is not found:", err)
except AttributeError as err:
    print("speed is not found:", err)
else:
    print("Executed succeed without errors")
finally:
    print("Final step")

print("==============")

try:
    print("passed here")
    a = car_dict.speed
    result = car_dict["year"]
    print("result", result)
except (KeyError, AttributeError) as err:
    print("Error:", err)
else:
    print("Executed succeed without errors")
finally:
    print("Final step")

print("==============")
try:
    print("passed here")
    a = car_dict.speed
    result = car_dict["year"]
    print("result", result)
except Exception as err:
    print("General Error:", err)
else:
    print("Executed succeed without errors")
finally:
    print("Final step")

# print(dir(__builtins__))

# result = car_dict["origin"]
# print("result", result)
