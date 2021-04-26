class Car():
  
    def __init__(self):
        self.engine = None
        self.price = None
        self.maxspeed = None
    def __str__(self):
        return '{} | {} | {}'.format(self.engine, self.price, self.maxspeed)      
 
class AbstractBuilder():

    def __init__(self):
        self.car = None
    def createNewCar(self):
        self.car = Car()
 
# Concrete Builder: inherits the Abstract Builder and implements the above interface createNewCar of the Abstract Builder class for a car object i.e. to say that
# its object is capable of creating a car by calling createNewCar() of AbstractBuilder; provides methods to create components of the product.
class ConcreteBuilder(AbstractBuilder):
    def addEngine(self):
        self.car.engine = "16 Cylynder"
    def addprice(self):
        self.car.price = "20000"
    def addmaxspeed(self):
        self.car.maxspeed = "300 Kms"
 
# Director: in charge of building the product using an object of Concrete Builder
class Director():
  
    def __init__(self, builder):
        self._builder = builder
    def constructCar(self):
        self._builder.createNewCar()
        self._builder.addEngine()
        self._builder.addprice()
        self._builder.addmaxspeed()
    def getCar(self):
        return self._builder.car
 
concreteBuilder = ConcreteBuilder()
director = Director(concreteBuilder)
 
director.constructCar()
carOne = director.getCar()
print("Car Details:", carOne)
 
carTwo = director.getCar()
print("Car Details:", carTwo)
