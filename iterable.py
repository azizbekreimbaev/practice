print("====== Iterable objects and RANGE =======")
# Iterable objects ==> string dict tuple list range map filter

# text = "MIT42"
for item in "MIT42":
    print(f"the letter: {item}")

range_obj = range(9)  # [0, 9)
print(range_obj)

for item in range_obj:
    print(f"values: {item}")

print("====== Dictionary =======")

# Dictionary is JSON object!

person = {
    "name": "Kevin",
    "age": 25
}

person_obj = dict(name="MIT", number="1000")

print(f"Person 1 info: {person}")
print(f"Person 2 info: {person_obj}")


# name = person["name"]
# print(f"His name {name}")

# name2 = person_obj["hobby"]
# print(f"hobby {name2}")        #cons: dictionary ichida yoq bolgan object qidirsak error berar ekan

# Dictionary bilan birga built in methodlar bor ishlash uchun
# method: get()

name = person_obj.get("name")
hobby = person_obj.get("hobby")
balance = person_obj.get("balance", "USD")

# bu method plus tarafi yoq bolsa ham eroor emas None qaytaradi
# agar mavjud bolmasa biz bergan qiymat qaytarishi uchun degaul argument berib ketsak bolar ekan get methodda
print(f"name: {name}, hobby: {hobby}")
print(f"agar mavjud bolmasa biz bergab qiymat qaytarsin {balance}")


# del person_obj["number"]  #object ichidagi state ochirish mumkin
for key in person_obj:
    # print(key)
    print(f"the key: {key} ==> value {person_obj[key]}")




