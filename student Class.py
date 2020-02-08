class Student:
    """Represents a student """
    population = 0

    def __init__(self, name, age, section):
        """Initializes the info"""

        self.name = name
        self.age = age
        self.section = section

        print("(Dislpaying\t  {})".format(self.name))

    def Register(self):
        Student.population += 1
        print("Name = {}".format(self.name))
        print("Age = {}".format(self.age))
        print("Class = {}\n".format(self.section))
    def Greeting(self):

        print("Hi this is {}. Glad to see ya\n".format(self.name))

    def Transfer(self):
        """bYE BYE"""
        print("{} has transfered. Sayonada!!\n".format(self.name))
        Student.population -= 1

        if Student.population == 0:
            print("{} is the last student. Bye Sensei\n".format(self.name))

        else:
            print("There are still {:d} students in your class\n".format(Student.population))

    @classmethod
    def howmany(cls):
        """Gretting by a student"""

        print("There are total {:d} student in your class\n".format(Student.population))



student1 = Student("Mg Mg",14 , 'Bio')
student2 = Student("Ma Ni" , 15 , 'Bio')
student3 = Student("Mg Zaw" , 14 , 'Eco')
student4 = Student("Ryan",15,'History')

student1.Register()
student2.Register()
student3.Register()
student4.Register()

student1.Greeting()
student2.Greeting()
student3.Greeting()
student4.Greeting()
Student.howmany()
student1.Transfer()
student2.Transfer()

student3.Transfer()
student4.Transfer()
Student.howmany()