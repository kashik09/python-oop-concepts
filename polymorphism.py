# POLYMORPHISM: Same method call, different behavior based on object type

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says: Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")


# Demo - Polymorphism in action
print("=== Polymorphism Demo ===")

# Create a list of different Animal objects
animals = [
    Dog("Buddy", 3),
    Cat("Asteroid Destroyer", 5),
    Dog("Max", 5),
    Cat("Luna", 1),
]

# Same method call on different types - each responds differently
for animal in animals:
    animal.speak()
