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

    def speak(self):
        print(f"{self.name} says: Hello!")
    
class Dog(Animal):
    def bark(self):
        print(f"{self.name} says: Woof!")

dog1 = Dog("Buddy", 3)
dog1.speak()  # Inherited method from Animal
dog1.bark()   # Method from Dog class

class Cat(Animal):
    def meow(self):
        print(f"{self.name} says: Meow!")

cat = Cat("Asteroid Destroyer", 5)
cat.speak()  # Inherited method from Animal
cat.meow()   # Method from Cat class
