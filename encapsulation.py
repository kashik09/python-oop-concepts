# ENCAPSULATION: Private attributes with getters/setters for controlled access

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age):
        self._name = name  # Private attribute
        self._age = age    # Private attribute

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


# Demo - Encapsulation in action
print("=== Encapsulation Demo ===")
dog = Dog("Buddy", 3)
cat = Cat("Asteroid Destroyer", 5)

# Using getters to access private attributes
print(f"Dog: {dog.name}, Age: {dog.age}")
print(f"Cat: {cat.name}, Age: {cat.age}")

# Using setters to update values
dog.name = "Max"
dog.age = 7
print(f"Updated dog: {dog.name}, Age: {dog.age}")

# Validation prevents bad data
print("\nTrying invalid values:")
try:
    cat.age = -5
except ValueError as e:
    print(f"Error: {e}")

try:
    dog.name = 123
except ValueError as e:
    print(f"Error: {e}")
