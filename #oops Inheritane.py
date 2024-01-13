#oops Inheritane


class Animal():   #base class
    def __init__(self) -> None:
        print("animal creating")
    
    def who_am_i(self):
        print("im human")

    def eat(self):
        print("im eating")



class Dog(Animal):  #child class who inherits the properties of base class
                        #parent class Animal

    def __init__(self):
        Animal.__init__(self)
        print("dog created")

    def who_am_i(self):
        print("im animal")
    
    def bark(self,nam):
        print("woof! my name is {} ".format(nam))


myanimal=Animal()
print(myanimal.who_am_i())

mydog=Dog()
print(mydog.who_am_i())


print(mydog.bark("tom"))