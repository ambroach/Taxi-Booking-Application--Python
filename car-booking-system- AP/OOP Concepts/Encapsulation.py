class SportsCars:
    Speed = 200
    Mileage = 50

class Chevy(SportsCars):
    def __init__(self):
        print(self.Speed)
    print(self.Mileage)

Chev = Chevy()

print(Chev.Speed)
print(Chev.Mileage)