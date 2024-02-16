""" Make a code that allows you feed and walk with a pet based on an animal group, that could both cats and dogs """ 
class Animal:

    def __init__(self, name, race): 
      self.name = name
      self.race = race

    def pasear(self):
        pass
    def alimentar(self):
        pass

class Pet(Animal):
    """def __init__(self, name, race, owner):
        #heredar los atributos de otras clases
        super.__init__(Animal, name,race)
    """
    def __set_owner__(self, owner):
        self.owner = owner

#offsprings example
class Cat(Pet):
    def pasear(self):

        print("Paseando al gato")

    def alimentar(self):
        print("Alimentando al gato")

class Dog(Animal):

    def pasear(self):
    
        print("Paseando al perro ", self.name, " de raza ", self.race )

    def alimentar(self):
        print("Alimentando al perro ", self.name, " de raza ", self.race)     

class Lizzard(Animal):

    def pasear(self):
        
        print("Paseando al lagarto ", self.name, " de raza ", self.race )

    def alimentar(self):
        print("Alimentando al lagarto ", self.name, " de raza ", self.race)  



if __name__ == '__main__':
#se crea instancias con los atributos establecidos en la clase   
 we = Pet("gato :D", "voss") 
 we.__set_owner__("manuel")
""" mascotas = [Dog("Fifi", "perro sucio"),Cat(we) , Lizzard("Moe", "Charmander")]
#se realiza los metodos de las estancias anteriores    
 for i in mascotas:
       i.pasear()
       i.alimentar()
   """  
we.pasear()
