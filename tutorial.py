class Student:
    highest = 240
    def __init__(self,phy,chem,maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
        self.total = phy + maths + chem
        if(self.total > Student.highest):
            Student.highest = self.total
        

    @classmethod
    def set_highest_in_class(cls,value):
        cls.highest = value

    @staticmethod
    def print_anything(printMe):
        print(printMe)


std1 = Student(91,70,80)
print(Student.highest)
Student.print_anything('hello')