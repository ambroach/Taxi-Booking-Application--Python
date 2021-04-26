class Borg:
  
  
    __shared_state = dict()

    def __init__(self):
  
        self.__dict__ = self.__shared_state
        self.state = 'CarBooking'
  
    def __str__(self):
  
        return self.state
  

if __name__ == "__main__":
  
    Customer1 = Borg()    
    Driver = Borg()    
    Admin = Borg()    
  
    Customer1.state = 'SpotsCar' 
    Driver.state = 'CarPooling' 
    #Admin.state = 'We Nedd MONEYYY!!!'   
  
    print(Customer1)    
    print(Driver)    
  
    Admin.state = 'Pickup Point'  
                         

    print(Customer1)    
    print(Driver)    
    print(Admin)   