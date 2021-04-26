#Atempt to make an organizational hierarchy
class LeafElement:
	def __init__(self, *args):

		self.position = args[0]

	def showDetails(self):

		print("\t", end ="")
		print(self.position)

class CompositeElement:

	def __init__(self, *args):

		self.position = args[0]
		self.children = []

	def add(self, child):

		self.children.append(child)

	def remove(self, child):

		self.children.remove(child)

	def showDetails(self):

		print(self.position)
		for child in self.children:
			print("\t", end ="")
			child.showDetails()
if __name__ == "__main__":
	topLevelMenu = CompositeElement("Admin")
	subMenuItem1 = CompositeElement("Pool Driver 1")
	subMenuItem2 = CompositeElement("Pool Driver 2")
	subMenuItem11 = LeafElement("Passenger")
	subMenuItem12 = LeafElement("Passenger")
	subMenuItem21 = LeafElement("Passenger")
	subMenuItem22 = LeafElement("Passenger")
	subMenuItem1.add(subMenuItem11)
	subMenuItem1.add(subMenuItem12)
	subMenuItem2.add(subMenuItem22)
	subMenuItem2.add(subMenuItem22)

	topLevelMenu.add(subMenuItem1)
	topLevelMenu.add(subMenuItem2)
	topLevelMenu.showDetails()
