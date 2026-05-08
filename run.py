# Dunder __builtins__, __init__

messaga = "PYTHON: Everything is object!"
print(messaga)

result = type(messaga)

print(result)

'''
In Python, there are built in tools:
(1) TYPES => int str float list dict
(2) FUNCTIONS => print() len() input() type() str() int()
(3) CONSTANTS => True False None
'''
print(dir(__builtins__))
