''' LOOPs
(1) for
(2) break/else
(3) while
'''

print("====== for operator =======")
# iterable objects ==> str int list dict tuple range map filter

text = "MIT42"
num = [10, 3, 4, 8]
car = dict(brand="Ferrari", year=2025)
range_obj = range(5)

for letter in text:
    print(f"the letter: {letter}")

print("========")

for numbers in num:
    print(f"the numbers: {numbers}")

print("========")

# for x in range_obj:
#     print(f"the nmums: {x}")

for x in range(1, 20, 9):
    print(f"the nmums: {x}")

print("========")

for key in car:
    print(f"the key: {key}, value ==> {car.get(key)}")

print("========")


print("====== break/else =======")

for x in range(1, 20, 9):
    print(f"the nums: {x}")
    if x > 10:
        print("Reached break")
        break
    else:
        print("Looped fully")

print("========")


print("====== while operator =======")

numb = 40

while numb > 0:
    numb -= 10
    print(f"number equals {numb}")

print("========")


steps = 0

while True:
    steps += 1
    x = int(input("Find number: "))

    if x == 41:
        print(f"You found number in {steps} steps")
        break
