class Vehicle:
    def type(self):
        print("automobile fall under vehicles")

class Cab(Vehicle):
    def type(self):
        print("yellow cars fall under here")

class Bus(Vehicle):
    def type(self):
        print("public transport")

x=Vehicle()
x.type()
S
y=Cab()
y.type()

z=Bus()
z.type()