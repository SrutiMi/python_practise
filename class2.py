class Student:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.lap = self.Laptop()

  def show(self):
    print(self.name , self.age)

  
  class Laptop:

    def __init__(self):
      self.brand = 'HP'
      self.cpu = 'i5'
      self.ram = 8


s1=Student('Sruti',20)

s1.show()
lap1 = s1.lap
print(s1.lap.brand)
print(lap1.brand)