class DeluxeInterface:
    def givedeluxeRide(self):
        pass

class PremiumInterface:
    def givePremiumRide(self):
        pass


class CarDeluxRide(DeluxeInterface):
    def giveDeluxeRide(self):
        print("Delux car ride")

class CarPremiumRide(PremiumInterface):
    def giveDeluxeRide(self):
        print("Premium car ride")
        