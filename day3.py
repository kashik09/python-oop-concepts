class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} says: Hello!")
    
class Dog(Animal):
    def bark(self):
        print(f"{self.name} says: Woof!")

dog1 = Dog("Buddy", 3)
dog1.speak()  # Inherited method from Animal
dog1.bark()   # Method from Dog class