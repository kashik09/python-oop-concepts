# ENCAPSULATION: Private attributes + getters/setters for safe access

class Animal:
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


class Dog(Animal):
    def speak(self):
        print(f"{self.name} says: Woof!")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")


# Demo
print("=== Encapsulation Demo ===")
dog = Dog("Buddy", 3)

# Getter
print(f"Name: {dog.name}")

# Setter with validation
dog.name = "Max"
print(f"Updated: {dog.name}")

# Validation blocks bad data
try:
    dog.age = -5
except ValueError as e:
    print(f"Error: {e}")
