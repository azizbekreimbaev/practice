'''CLASS DEEP
(1) Encapsulation
(2) Inherintance
(3) Polimorphism
'''
print("======= Inherintance ========")
# PARENT ==> CHILD == STATE | METHOD


class Animal:
    description = "The class creates animals"

    def __init__(self, voice):
        self.voice = voice
        self._status = "is alive"

    def make_voice(self):
        print(f"This animal makes voice {self.voice}")


class Dog(Animal):

    def __init__(self, name, sound, voice):
        super().__init__(voice)
        self.name = name
        self.sound = sound

    def introduce(self):
        print(f"{self.name} says: {self.voice} - {self.voice}")

    def protect(self):
        print("Dog can protect")

    def make_voice(self):
        print(f"This animal makes voice {self.sound}")


class Cat(Animal):

    def __init__(self, name, sound, voice):
        super().__init__(voice)
        self.name = name
        self.sound = sound

    def introduce(self):
        print(f"{self.name} says: {self.voice} - {self.voice}")

    def play(self):
        print("Cats play")

    def make_voice(self):
        print(f"This animal makes voice {self.sound}")


class Fish(Animal):

    def __init__(self, name, sound, voice):
        super().__init__(voice)
        self.name = name
        self.sound = sound

    def introduce(self):
        print(f"{self.name} says: {self.voice} - {self.voice}")

    def swim(self):
        print("Fish can swim")


dog = Dog("Belka", "wow", True)
cat = Cat("Tom", "meow", True)
fish = Fish("Nemo", "ZZzzzZZ", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("=======")

dog.make_voice()
cat.make_voice()
fish.make_voice()

print(Animal.description)

print(dog.voice, fish.voice)

print(dog._status)


print("======= Inherintance ========")

dog.make_voice()
cat.make_voice()


print("====================")

# fish ==> Fish ==> Animal ==> object
a = isinstance(fish, Fish)
b = isinstance(fish, Animal)
c = isinstance(fish, object)
d = isinstance("MIT42", object)
print("result", a)
print("result", b)
print("result", c)
print("result", d)

data = issubclass(Fish, Animal)
print("result", data)
