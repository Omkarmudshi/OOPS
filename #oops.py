#oops 1

class Dog():
    def __init__(self,bread,name,spot):
        #string
        self.bread=bread
        self.dog_name=name
        #boolean T/F
        self.spot=spot

mysample= Dog(bread='lab',name="babu",spot=True)

print(mysample.bread)
print(mysample.dog_name)
print(mysample.spot)