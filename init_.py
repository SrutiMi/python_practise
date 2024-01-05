class Computer:
  def __init__(self,cpu,ram):
    self.cpu = cpu
    self.ram = ram
    # self.c = cpu
    # self.r = ram
    
  def config(self):
    print(self.c, self.r)

com1 = Computer('i5', 16)
com1.config()
print(type(com1))