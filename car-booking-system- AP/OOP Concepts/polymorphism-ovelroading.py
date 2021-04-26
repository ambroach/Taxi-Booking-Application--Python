class rent:

    def details(self, price=None):
    
        if price is not None:
            print('My rent - ' + price)
        else:
            print('you the car for free')

x=rent()

x.details()

x.details("1000")