# POLYMORPHISM: Same method, different behavior

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print(f"{self.name} says: Woof!")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")


# Demo
print("=== Polymorphism Demo ===")

animals = [
    Dog("Buddy", 3),
    Cat("Asteroid Destroyer", 5),
    Dog("Max", 5),
    Cat("Luna", 1),
]

# Same method call, different behavior
for animal in animals:
    animal.speak()
