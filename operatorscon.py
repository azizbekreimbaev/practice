'''OPERATORS and CONDITIONS
(1) Operators
(2) Condition
(3) Logical Operators
'''

print("====== Operators ======")
# + - < > >= <= == * is /          // % += **


a = 23
b = 5
print(a/b)
result = a // b
left = a % b
print(f"the result: {result} and left: {left}")

a += 100
print(a)
print("b ning kvadrati:", b**2)
print("b ning kubi:", b**3)

c = dict(name="Kevin", age=25)
d = dict(name="Kevin", age=29)
e = c

print(c == d)  # only compares value
print(id(c), id(d), id(e))

data = c is d
print("c is d", data)
print("c is e", c is e)

print("======= Conditions ======")

x = 5

if x > 50:
    print("Case A")
elif x > 10:
    print("Case B")
else:
    print("Case C")


print("======= Logical Operator ======")
age = 25
# person = None
# if age > 16:
#     person = "adult"
# else:
#     person = "child"

# print("person:", person)

# Ternary
person = "adult" if age > 18 else "teen"
print("person:", person)

print("===============")
is_student = True
is_admin = False
is_guest = True
is_parent = True

if not is_student:
    print("Welcome heree, you wnat to be a styudent")
elif is_admin:
    print("Please go to this office")
elif is_guest or is_parent:
    print("Waiting room")
else:
    print("Other Cases")