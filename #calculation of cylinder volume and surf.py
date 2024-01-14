#calculation of cylinder volume and surface

class Cylinder():

    pi=3.14
    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius

    def volume(self):
        
        v=self.pi*self.radius**2*self.height
        return v
    def surface(self):
        s=(2*self.pi*self.radius*self.height)+(2*self.pi*self.radius**2)
        return s
    
h=2
r=3 
mycly=Cylinder(h,r)
print(mycly.volume())
print(mycly.surface())
        