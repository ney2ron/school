#-*- coding: cp1251 -*-
class Shape ():
    def __init__ (self, w,l):
        self.width = w
        self.len = l
        
    def print_size(self):
        print(""" {} и {} """.format(self.width, self.len))
        
    def treugl (self,h):
        self.hight = h
        print("""Треуголник со сторонами: Ширина {} , Высота {} и Длинна {} """
              .format(self.width, self.len, self.hight ))
        
        




my_shape = Shape(20,25)
my_shape.print_size()
my_treugl = Shape(13,19)
my_treugl.treugl(7)
