# INHERITANCE: Child classes inherit from parent class

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} makes a sound")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} says: Woof!")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")


# Demo
print("=== Inheritance Demo ===")
dog = Dog("Buddy", 3)
cat = Cat("Asteroid Destroyer", 5)

# Inherited from Animal
print(f"{dog.name} is {dog.age} years old")
print(f"{cat.name} is {cat.age} years old")

# Overridden speak()
dog.speak()
cat.speak()
