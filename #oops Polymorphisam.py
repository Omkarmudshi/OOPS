#oops Polymorphisam

class Dog():
    def __init__(self,name):
        self.name=name
    def speck(self):
        return self.name + (" say woof")
    
class Cat():
    def __init__(self,name):
        self.name=name
    def speck(self):
        return self.name + " say meoww"
    
tom=Dog("Tom")
rani=Cat("rani")
print(tom.speck())
print(rani.speck())

for pet in [tom,rani]:
    print(pet.speck())

class Animal():
    def __init__(self,name):
        self.name=name

    def speak(self):            #abstrack method
        raise NotImplementedError("subclass must implement this abstract method ")   #error excepsion
    

class Dog(Animal):
    def speak(self):
        return self.name + " woof"
    
class Cat(Animal):
    def speak(self):
        return self.name + " meowww"
    
zoro=Dog("zoro")
nami=Cat("nami")

print(zoro.speak())
print(nami.speak())
        
#myanimal=Animal("zoro")
#print(myanimal.speak())
