class SchoolMember:
    """Represents any school member."""

    def __init__(self, name , age):
        self.name = name
        self.age = age
        print("Initialized SchoolMember: {}".format(self.name))

    def tell(self):
        """Tell my details"""
        print('Name:"{}" Age:"{}"',format(self.name,self.age) , end="")

class Teacher(SchoolMember):

    def __init__(self , name , age ,marks):
        SchoolMember.__init__(self , name , age)
        self.marks = marks
        print('(Initialized Stduent: {})'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print("Msrks: '{:d}' ".format(self.marks))

class Teacher(SchoolMember):
    """Represents a student"""

    def __init__(self, name, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print("Initializes student:{}".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}" '.format(self.marks))

class Student(SchoolMember):
    """Represents a Student"""

    def __init__(self , name , age , marks):
        SchoolMember.__init__(self.name , age)
        print('Initialized Student:{}'.format(self.name))

        def tell(self):
            SchoolMember.tell(self)
            print('Marks:"{:d}"'.format(self.marks))

t = Teacher('Mrs.Waasakaka',40 )
s = Student("Shakaa" , 25 , 75)

print()
members = [t,s]
for member in members:
	member.tell()
