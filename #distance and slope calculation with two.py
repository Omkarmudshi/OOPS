#distance and slope  calculation with two co-ordinates


class Line():
    def __init__(self,coor1,coor2):
           self.coor1=coor1
           self.coor2=coor2
    def distance(self):
          x1,y1=self.coor1
          x2,y2=self.coor2
          d=(((x2-x1)**2)+((y2-y1)**2))**0.5
          return d
    def slope(self):
          
        x1,y1=self.coor1
        x2,y2=self.coor2
        s=y2-y1/x2-x1
        return s

c1=(3,2)
c2=(8,10)
dist=Line(c1,c2)
print(dist.distance())
print(dist.slope())
