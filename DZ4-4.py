#-*- coding: cp1251 -*-
class Hors():
    def __init__ (self, name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner
        
class Rider():
    def __init__ (self, name):
        self.name = name
        
jeck = Rider("���� �����")
mustang = Hors("�������","������",jeck)
print(mustang.owner.name,mustang.breed)