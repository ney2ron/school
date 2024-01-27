# -*- coding: cp1251 -*-
class Square:
    square_list = []
    def __init__(self,w):
        self.width = w
        #self.len = l
        self.square_list.append((self.width))
        
    def print_size (self):
        print(""" {} на {} на {} на {} """.format(self.width,self.width,self.width,self.width))

fart = Square(29)
print(fart.square_list)
print(fart.print_size())