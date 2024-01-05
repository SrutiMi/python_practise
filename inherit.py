class A:
  def feature1(self):
    print("Feature 1 working")
  def feature2(self):
    print("Feature 2 working")

class A2:
   def feature12(self):
     print("Feature 1-A2 working")

# example of single level inheritance
class B(A):

  def __init__(self) :
    super().__init__()#calling the constructor of parent class

  def feature3(self):
    print("Feature 3 working")
  def feature4(self):
    print("Feature 4 working")

# example of multi level inheritance
class C(B):
  def feature5(self):
    print("Feature 5 working")


#example of multiple level inheritance
class D(A, A2):
  def feature6(self):
    print("Feature 6 working")


a1= A()
a1.feature1()

b1=B()
b1.feature1()


