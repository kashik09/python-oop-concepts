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

dog = Dog("Buddy", 3)
dog.speak()  # Dog's implementation of speak()

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")

cat = Cat("Asteroid Destroyer", 5)
cat.speak()  # Cat's implementation of speak()
