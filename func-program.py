# -*-coding: cp1251 -*-

class Orange():
    def __init__ (self, w, c):
        """ ��� � ������� """
        self.weight = w
        self.color = c
        self.mold = 0
        print("�������!")
    def rot (self, days, temp):
        self.mold = days * temp
        
orange = Orange(6, "��������")
print(orange.mold)
orange.rot(10,33)
print(orange.mold)
    