class Driving:
	'''Subsystem # 1'''

	def wash(self):
		print("Driving")


class Rinsing:
	'''Subsystem # 2'''

	def rinse(self):
		print("PickUp")


class Spinning:
	'''Subsystem # 3'''

	def spin(self):
		print("Drop Off")


class DrivingMachine:
	'''Facade'''

	def __init__(self):
		self.Driving = Driving()
		self.rinsing = Rinsing()
		self.spinning = Spinning()

	def startdriving(self):
		self.Driving.Driving()
		self.rinsing.rinse()
		self.spinning.spin()

""" main method """
if __name__ == "__main__":

	DrivingMachine = DrivingMachine()
	DrivingMachine.startdriving()
