class TAXI:
    
    def __init__(self, num):
        self.num = num
        
    def ride_along(self):
        print("You may want to get in" + self.num)
        
class TAXIPool(TAXI):

    def ride_along(self):
        print("You want a pool ride? ") 
        print(self.num + " will take care of that with our srvices")

y = TAXIPool("Shah and Shah")
y.ride_along()