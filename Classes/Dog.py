#Dog.py

class dog:
	def __init__(self  ,  name , color , owner , age):
		self.name = name
		self.color = color
		self.owner = owner
		self.age = age
		

	
	def dog(self):
		print('Dog is ' , self.name)
	def colour(self):
		print('It\'colorr is ' , self.color)
	def owner(self):
		print('His owner is' , self.owner)
	def age(self):
		print('Age is ' , self.age)


d = dog('Aung Net' , 'Black' , 'U Kaung' , 2)

d.colour()
d.age()

