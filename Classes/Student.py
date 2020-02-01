class SchoolMember:

	def __init__(self, name , marks):
		self.name = name
		self.age  = age
		print('(Initialized SchoolMember:{}'.format(self.name))
	def tell(self):
		SchoolMember.tell(self)
		print("Initializes student:{}".format(self.name))
		


class Teacher(SchoolMember):
	"""Represents a student"""

	def __init__(self, name , marks):
		SchoolMember.__init__(self , name , age)
		self.marks = marks
		print("Initializes student:{}".format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Marks: "{:d}" '.format(self.marks))

class Student(SchoolMember)
	'''REPRESENTS A STUDENT'''

	def __init__(self,name,age,marks):
		SchoolMember.__init__(self,name,age)
		print('Initialized Student:{}'.format(self..name))
	def tell(self):
		SchoolMember.tell(self)
		print('Marks:"{:d}"'.format(self.marks))


t = Teacher('Mrs. Waasakaka',40 , 30000)
s = Student('Shakaa' , 25 , 75)

print()

members = [t,s]
for member in members:
	member.tell()