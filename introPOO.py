""" Make a code that allows you feed and walk with a pet based on an animal group, that could both cats and dogs """ 
class Animal:

    def __init__(self, name, race): 
      self.name = name
      self.race = race

    def pasear(self):
        pass
    def alimentar(self):
        pass

#offsprings example
class Cat(Animal):
    def pasear(self):

        print("Paseando gato")

    def alimentar(self):
        print("Alimentando gato")

class Dog(Animal):

    def pasear(self):
        print("Paseando perro")

    def alimentar(self):
        print("Alimentando perro")       

