#-*- coding: cp1251 -*-
class Lion:
    def __init__ (self, name):
        self.name = name
        
    def __repr__(self):
        return self.name
        
lion = Lion("�������")
print(lion)