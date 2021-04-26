class Sedean:
	def __init__(self):
		self.name = "Sedean"

	def FourSeater(self):
		return "FourSeater"

class SUV:

	def __init__(self):
		self.name = "SUV"

	def EightWheeler(self):
		return "EightWheeler"

class MINI:

	def __init__(self):
		self.name = "MINI"

	def FourWheeler(self):
		return "FourWheeler"

class Adapter:

	def __init__(self, obj, **adapted_methods):
		self.obj = obj
		self.__dict__.update(adapted_methods)

	def __getattr__(self, attr):
		return getattr(self.obj, attr)

	def original_dict(self):
		return self.obj.__dict__

if __name__ == "__main__":
	objects = []

	Sedean = Sedean()
	objects.append(Adapter(Sedean, wheels = Sedean.FourSeater))

	SUV = SUV()
	objects.append(Adapter(SUV, wheels = SUV.EightWheeler))

	MINI = MINI()
	objects.append(Adapter(MINI, wheels = MINI.FourWheeler))

	for obj in objects:
        print("A {0} is a {1} vehicle".format(obj.name, obj.wheels()))
