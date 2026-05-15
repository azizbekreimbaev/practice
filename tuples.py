'''Tuple
(1) What is tuple vs list
(2) Unpacking arguments
(3) zip
'''

print("========== What is tuple vs list ==========")

# Java/PHP/NodeJs array ==> Python list

# literal
nums = [2, 3, 41, 33]
print(nums)
car = {"brand": "Ferrari"}
# constructor

letters = list("Hello World")
print(letters)
person = dict(name="Kevin", age=25)

# list larda qiymatlarni ozgartirish mumkin ekan
fruits = ["apple", "lemon", "banana", "kiwi"]
print(f"before fruits", fruits)

fruits[2] = "melon"
print(f"after fruits", fruits)

# tuple esa qiymatlarni ozgartirib bolmaydi

animals = ("dog", "cat", "fish", "lion")

# xar xil data typelarni kiritsa bolar ekan bitta tuple ichida
tuple_obj = ("MIT", 200, True, None)

print(animals[0])
# animals[0] = "bird"  TypeError: 'tuple' object does not support item assignment


print("========== Unpacking arguments ==========")

# unpackuing by tuple
# try avoid this
# people = "Kevin", "Fede"
# animals = "dog",

groups = ["MIT", "FLEXY", "DEVEX", "MG"]
# distraction argumentlarni yoyish uchun tuple ishlatiladi

(x, y, z, a) = groups
(x, y, *z) = groups
print(f"the x: {x} and y: {y}")

print(f"the z: {z}")  # list


# *args ===> tuple

def calc(*args):
    print(args)
    total = 1
    for x in args:
        total *= x
    print(f"the type (*args): {type(args)}")
    print(f"the total value: {total}")
    return total


# CALL
calc(1, 2, 3, 4)
calc(1, 0, 3, 4)
calc(3, 4)

# **kwargs ==> dictionary orqali unpacking


def intro(**kwargs):
    print(f"type(**kwargs) value: {type(kwargs)}")
    print(f"I am {kwargs["name"]} and I am {kwargs["age"]} years old")
    pass


intro(name="kevin", age=25)  # berilayotgan argumentlarimiz miqdori noaniq bolsa bu dictionary unpacking bilan unpack qilamiz
