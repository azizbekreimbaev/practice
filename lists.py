'''List
(1) Working with lists
(2) List methods
(3) Lambda functions
(4) enumarate, map and filter
'''

print("============ Working with lists ==============")

# Java/PHP/NODEjs array ==> Python list

# literal
person = {"name": "justin", "age": 25}  # dictionary
people = ("Andrew", "John", "Micheal")  # tuple
groups = ["MIT", "FLEXY", "DEVEX", "MG"]  # list

for team in groups:
    print(F"Teams are: {team}")

# constructor usuli bilan arraylarni hosil qilish

letters = list("Hello world!")
print(f"the letters: {letters} and size: {len(letters)}")

print("=====================")

fruits = ["apple", "orange", "lemon", "kiwi"]

a = fruits[0]
b = fruits[0:2]  # [0, 2)
c = fruits[::3]  # 3 step tashab qiymat qaytaradi
d = fruits[::-1]

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

print("============ List methods ==============")

# methods ==>  append() insert() pop() remove() clear() sort() index()

letters = ["a", "b", "e"]

letters.append("f")  # add to the end
print("=====================")

print(letters)

letters.insert(0, "z")  # add to the start
print(letters)
print("=====================")

size = len(letters) - 1
result = letters.pop(size)  # pop  cuts from end
print(result)
print("=====================")
print(letters)
print("=====================")

result2 = letters.pop(0)  # cuts from start
print(result2)
print("=====================")

animals = ["dog", "cat", "fish", "lion"]
animals.remove("lion")
print(animals)
print("=====================")

del animals[2:3]
print(animals)

print("=====================")

exist = animals.index("cat")  # value errorni consider qilishimiz kerak
print("cat index:", exist)
print("=====================")

animals.clear()
print("animals:", animals)

# exist = animals.index("cat")  # value errorni consider qilishimiz kerak
# print("cat index:", exist)


if "cat" in animals:
    print("index cat:", animals.index("cat"))
else:
    print("that value is not exsits")

print("=====================")

nums = [2, 3, 44, 52, 42]

nums.sort()
print(nums)
print("=====================")
nums.sort(reverse=True)
print(nums)
print("=====================")

# immutable methods sorted()/index() kerak bolsa specific
nums2 = [112, 213, 44, 52, 42]

new_numbers = sorted(nums2)

print(new_numbers)
print(nums2)


print("============ Lambda function ==============")
# labmda is small anonymous function


def calc(x, y): return x*y


result = calc(3, 4)
print(result)
print("=====================")

people = [
    ("Robert", 20),
    ("Kevin", 25),
    ("Fede", 43),
    ("Ali", 53)
]
# sorting by age
people.sort()
print(people)

# sort by age by lambda
people.sort(key=lambda person: person[1])
print(people)

print("============ enumerate, map and filter ==============")
# enumerate  provides both index and value at once

animals = ["dog", "cat"]  # list
for item in enumerate(animals):
    print(item)
print("=====================")

for (index, value) in enumerate(animals):
    print(f"index: {index} and value: {value}")
print("=====================")


# similar in dictionary

car = dict(brand=" MERC", year=2026)

# result = car.get("brand")
result = car.items()
print(result)
print("=====================")

for (key, value) in result:
    print(f"key: {key} and value: {value}")

print("=====================")

#   map
cars = [
    ("Ferrari", 78),
    ("Tayota", 178),
    ("Audi", 98),
    ("BMW", 18),
    ("Chevrolet", 278),
]

# task bu yerda moshina brand nomlarini yani araayga hosil qilish

# new_car = []

# for car in cars:
#     new_car.append(car[0])
# print(new_car)


result1 = map(lambda car: car[0], cars)  # map qilib olib
print(result1, type(result1))

print("=====================")
new_cars = list(result1)  # mapnio listga transfer qilamiz
print(new_cars)

print("=====================")

# filter

result_filter = filter(lambda car: car[1] > 80, cars)
print(result_filter, type(result_filter))
print(list(result_filter))
