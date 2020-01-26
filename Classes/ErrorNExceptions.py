#python ErrorNExceptions.py

# class Person:
# 	def say_hi(self):
# 		print('Hello , how are you?')

# p = Person()
# p.say_hi()

#__init__method

class Person:
	def __init__(self , name , age ,code , gender):
		self.name = name
		self.age = age 

	def say_hi(self):
		print('Hello my name is ' , self.name  )

	def say_age(self):
		print('I\'m' , self.age)

p = Person('Swaroop' , 34 , 1675 , 'male')
p.say_hi()
p.say_age()




