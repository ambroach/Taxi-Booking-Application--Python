class Car(object):

    def factory(type):
        if type == "Racecar":
            return Racecar()
        if type == "minibus":
            return minibus()

    factory = staticmethod(factory)

class Racecar(Car):
    def drive(self):
        print("Racecar driving.")

class minibus(Car):
    def drive(self):
        print("minibus driving.")

# Create object using factory.
obj = Car.factory("Racecar")
obj.drive()