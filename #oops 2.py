#oops 2


class Dog():
    #class object attribute
    spacise='animal'

    def __init__(self,bread,name):
        self.bread=bread
        self.name=name
    #operations/action--->method
    def bark(self):
         return ("woof! my name is {} and the number is ".format(self.name))

my_dog=Dog(bread="lab",name="tom")
print(type(my_dog))

print(my_dog.bread)
print(my_dog.name)
print(my_dog.spacise)
print(my_dog.bark())

##########################################################


class Circle():

    #class object attribute
    pi=3.14

    def __init__(self,radius):
        self.radius=radius
        self.area=radius*radius*Circle.pi
        self.area1=radius*radius*self.pi
    
    #method
    def get_circumferance(self):
        return self.radius * self.pi *2
    
rad=int(input("enter circle radius of circle "))
result=Circle(rad)
print(result.pi)
print(result.radius)
print(result.area)
print(result.area1)
print(result.get_circumferance())