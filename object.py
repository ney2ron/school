#-*- coding: cp1251

class Apple ():
    """ �������� ����� """
    def __init__(self, weith, color):
        self.weith = weith
        self.color = color
        
    def days_of_collecting (self, days):
        self.days = days
        
    def taste_fruit (self, fruit):
        self.fruit = fruit
        
Fruct = Apple(25,"�������")
print("����� ������: ")
print(Fruct.weith,"�������")
print(Fruct.color)
Fruct.days_of_collecting(6)
print(Fruct.days,":" ,"���� ����� ���� �������")
Fruct.taste_fruit("�������")
print(Fruct.fruit)