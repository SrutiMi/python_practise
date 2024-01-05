class Student:
   school= " CU"

   def __init__(self,m1,m2,m3):
      self.m1 = m1
      self.m2 = m2
      self.m3 = m3

   def avg(self):
      return (self.m1+self.m2+self.m3)/3
   
   @classmethod
   def infoSchool(cls):
      return cls.school
   
   @staticmethod #it has nothing to do with class and instances so we are using static methods
   def info():
      print("This is Student class")

s1 = Student(31,22,33)
s2 = Student(44,55,66)

print(s1.avg())
print(Student.infoSchool())
print(s2.avg())

Student.info()