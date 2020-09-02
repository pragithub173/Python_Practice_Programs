from math import *

class Student:

    def __init__(self, name, major, gpa):
        self.name = name,
        self.major = major,
        self.gpa = gpa

    def qualified(self):
        if self.gpa >= str(3.5):
            return True
        else:
            return False


student1 = Student("Pradeep", "CS", "3.33")
student2 = Student("Kumar", "BIO", "3.5")

print(student2.qualified())
