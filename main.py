class Pet:
    def __init__(self, name, species, age, gender):
        self._name = name
        self._species = species
        self._age = age
        self._gender = gender
        self._printing = {'name': self._name,
                    'gender': self._gender,
                    'species': self._species,
                    'age': self._age}
    def get_info(self):
        print()
        for key, value in self._printing.items():
            print(f'{key}: {value}')

    def speak(self, says=None):
        print(says)

class Dog(Pet):
    def __init__(self, name, age, gender, breed):
        super().__init__(name, "Dog", age, gender)
        self._breed = breed
        self._printing['breed'] = self._breed

    def speak(self, says='Woof!'):
        super().speak(says)




class Cat(Pet):
    def __init__(self, name, age, gender, color):
        super().__init__(name, "Cat", age, gender)
        self._color = color

    def speak(self, says='Meow!'):
        super().speak(says)

class Kitty(Cat):
    def __init__(self, name, age, gender, color):
        super().__init__(name, "Kitty", age, gender)
        self._color = color

    def speak(self, says='Sweet Meow!'):
        super().speak(says)


# create instances of the Dog and Cat classes
dog = Dog("Buddy", 2, "Male", "Golden Retriever")
cat = Cat("Fluffy", 3, "Female", "Calico")
kitty = Kitty("Tomy", 0.25, "Male", "Calico")
# call the methods on the objects to demonstrate inheritance, encapsulation, and polymorphism
dog.get_info()
dog.speak()
cat.get_info()
cat.speak()
kitty.get_info()
kitty.speak()