# PRIVATISATION: Use underscore prefix to make attributes private

class Animal:
    def __init__(self, name, age):
        self._name = name  # Private: use _ prefix
        self._age = age    # Private: use _ prefix

    def speak(self):
        print(f"{self._name} makes a sound")


class Dog(Animal):
    def speak(self):
        print(f"{self._name} says: Woof!")


class Cat(Animal):
    def speak(self):
        print(f"{self._name} says: Meow!")


# Demo
print("=== Privatisation Demo ===")
dog = Dog("Buddy", 3)
cat = Cat("Asteroid Destroyer", 5)

# Can still access (but shouldn't directly)
print(f"Dog's private name: {dog._name}")
print(f"Cat's private age: {cat._age}")

dog.speak()
cat.speak()
