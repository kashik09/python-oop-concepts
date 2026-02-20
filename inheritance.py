# INHERITANCE: Dog and Cat inherit from Animal base class

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


# Demo - Inheritance in action
print("=== Inheritance Demo ===")
dog = Dog("Buddy", 3)
cat = Cat("Asteroid Destroyer", 5)

# Dog and Cat inherited name and age properties from Animal
print(f"{dog.name} is {dog.age} years old")
print(f"{cat.name} is {cat.age} years old")

# Each overrides speak() in their own way
dog.speak()
cat.speak()
