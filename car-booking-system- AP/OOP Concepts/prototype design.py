import copy
 
class Car:
        '''Prototypical class'''
        def __init__(self):
              
                self.engine = "16 Cylynder"
                self.color = "Blue"
                self.capacity = "5"
        def __str__(self):
            
                return  '{} | {} | {}'. format(self.engine, self.color, self.capacity)

class Prototype:
        '''Prototype class'''
        def __init__(self):

                self._toBeClonedObjects = {}
        def registerObject(self, name, obj):
                
                self._toBeClonedObjects[name] = obj
        def unregisterObject(self, name):
             
                del self._toBeClonedObjects[name]
        def clone(self, name, **kwargs):
              
                clonedObject = copy.deepcopy(self._toBeClonedObjects.get(name))
                clonedObject.__dict__.update(kwargs)
                return clonedObject
 
defaultCar = Car()                                                     
prototype = Prototype()
prototype.registerObject('basicCar', defaultCar)           
 
carOne = prototype.clone('basicCar', capacity= '6', engine='32 Cylinders')                          
print("Car Details:", carOne)                             
 
carTwo = prototype.clone('basicCar', color = "Black")  
print("Car Details:", carTwo)                             