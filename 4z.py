
from random import triangular


class Triangle:
   def __init__(self, a, h):
      self.osn = a
      self.hiage = h
      
   def area(self):
      
      square = 1/2 * self.osn * self.hiage
      return square

tringle = Triangle(11,4)
print(tringle.area())
      

       

